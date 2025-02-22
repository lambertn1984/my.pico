#import modules
import network
import socket
from time import sleep
from machine import Pin, I2C
import bme280

#initialize I2C 
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# ... (your SSID, password, and I2C initialization)
ssid = 'berlin' #Your network name
password = '8pbn-4vrq-qa4e' #Your WiFi password

def webpage(temp, pressure, humidity):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Pico W Weather Station</title>
    <meta http-equiv="refresh" content="10">
    <style>
        body {{
            font-family: sans-serif;
            background-color: #f0f0f0; /* Light gray background */
        }}
        .container {{
            width: 80%;
            margin: 20px auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            text-align: center;
            color: #333; /* Darker text color */
        }}
        .reading {{
            font-size: 2em; /* Larger font size */
            margin-bottom: 10px;
        }}
        .image {{
            text-align: center; /* Center the image */
            margin-top: 20px;
        }}
        .image img {{
            max-width: 100px; /* Limit image width */
            height: auto;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <h1>Pico W Weather Station</h1>
        <div class="reading">Temperature: {temp}</div>
        <div class="reading">Pressure: {pressure}</div>
        <div class="reading">Humidity: {humidity}</div>
    </div>
    </body>
    </html>
    """
    return str(html)

def serve(connection):
    while True:
        temp = 999
        pressure = 999
        humidity = 999
        bme = bme280.BME280(i2c=i2c)
        temp = bme.values[0]
        pressure = bme.values[1]
        humidity = bme.values[2]

        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)

        html = webpage(temp, pressure, humidity)  # Pass individual values
        client.send(html)
        client.close()

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
    

#import modules
import network
import socket
from time import sleep
from machine import Pin, I2C, SoftI2C
import machine
import bme280
from bh1750 import BH1750

# from https://www.explainingcomputers.com/pi_pico_w_weather.html

ssid = 'berlin' #Your network name
password = '8pbn-4vrq-qa4e' #Your WiFi password

#initialize I2C
#DEL
led = machine.Pin("LED", machine.Pin.OUT)

# temp., press., hum.
i2c1 = SoftI2C(scl=Pin(13), sda=Pin(12), freq=400000)
bme = bme280.BME280(i2c=i2c1) # Initialize BME280 outside the loop
# light
i2c0 = SoftI2C(sda=Pin(14), scl=Pin(15))
bh1750 = BH1750(0x23, i2c0)


def connect():
    """
    Connects the Raspberry Pi Pico W to the specified Wi-Fi network.

    Returns:
        str: The IP address assigned to the Pico W.
    """
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
    """
    Opens a socket for network communication on the given IP address.

    Args:
        ip (str): The IP address to bind the socket to.

    Returns:
        socket.socket: The opened socket object.
    """
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(temp, pressure, humidity, light):
    """
    Generates an HTML webpage displaying the sensor readings.

    Args:
        temp (str): Temperature reading.
        pressure (str): Pressure reading.
        humidity (str): Humidity reading.
        light (int): Light intensity reading.

    Returns:
        str: The HTML content of the webpage.
    """
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
        <div class="reading">Light: {light}</div>
    </div>
    </body>
    </html>
    """
    return str(html)

def serve(connection):
    """
    Starts a web server that serves the sensor readings on a webpage.

    Args:
        connection (socket.socket): The socket connection to serve.
    """
    #Start a web server

    while True:
        led.value(0)
        bme = bme280.BME280(i2c=i2c1)
        temp = bme.values[0]
        pressure = bme.values[1]
        humidity = bme.values[2]
        light=bh1750.measurement
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        html = webpage(temp, pressure, humidity, light)
        client.send(html)
        client.close()
        sleep(1)  # Pause between repetitions (adjust as needed)
        led.value(1)

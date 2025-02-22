from time import sleep
from machine import Pin, I2C
import bme280

# Get the bme280.py file from https://github.com/SebastianRoll/mpy_bme280_esp8266/blob/master/bme280.py 
# and save it on the pico (with Thonny or rshell).

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(i2c=i2c)  # Initialize BME280 outside the loop

while True:
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values[2]

    # Convert values to strings and format the output
    temp_str = str(temp)
    pressure_str = str(pressure)
    humidity_str = str(humidity)

    print("Temperature:", temp_str)
    print("Pressure:", pressure_str)
    print("Humidity:", humidity_str)
    print("-" * 20)  # Separator for readability

    sleep(2)  # Adjust the delay as needed

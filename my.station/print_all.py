from time import sleep
from machine import Pin, I2C, SoftI2C
import bme280
from bh1750 import BH1750
import machine

# Print all the sensor together

###Initialize port
#
#DEL
led = machine.Pin("LED", machine.Pin.OUT)

# temp., press., hum.
i2c1 = SoftI2C(scl=Pin(1), sda=Pin(0), freq=400000)
bme = bme280.BME280(i2c=i2c1)  # Initialize BME280 outside the loop
# light
i2c0 = SoftI2C(sda=Pin(8), scl=Pin(9))
bh1750 = BH1750(0x23, i2c0)

while True:
    sleep(1)  # Pause between repetitions (adjust as needed)
    led.value(0)
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values[2]
    light=bh1750.measurement

    # Convert values to strings and format the output
    temp_str = str(temp)
    pressure_str = str(pressure)
    humidity_str = str(humidity)
    light_str = str(light)

    print("Temperature:", temp_str)
    print("Pressure:", pressure_str)
    print("Humidity:", humidity_str)
    print("Light:", light_str)
    print("-" * 20)  # Separator for readability

    sleep(1)  # Pause between repetitions (adjust as needed)
    led.value(1)


import machine
import utime

# This will blink the DEL every seconds
# Need to be saved as "main.py" in the pico. 

led = machine.Pin("LED", machine.Pin.OUT)

# Repeat the message indefinitely
while True:
    utime.sleep(1)  # Pause between repetitions (adjust as needed)
    led.value(0)
    utime.sleep(1)  # Pause between repetitions (adjust as needed)
    led.value(1)

import machine
import utime

# This will blink the DEL to make a Morse code for "Message". 
# Need to be saved as "main.py" in the pico. 

led = machine.Pin("LED", machine.Pin.OUT)

# Complete Morse code dictionary
morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..-..', '!': '-.-.--',
    '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', ' ': '/',  # Space
}

# blink_morse and blink_word functions (same as before)
def blink_morse(char):
    code = morse_code.get(char.upper())
    if code is None:
        print("Character", char, "not found in morse code dictionary.")
        return
    for dot_dash in code:
        if dot_dash == '.':
            led.value(1)
            utime.sleep(0.2)  # Short blink (dot)
        elif dot_dash == '-':
            led.value(1)
            utime.sleep(0.6)  # Long blink (dash)
        elif dot_dash == '/':  # word space
            led.value(0)
            utime.sleep(0.6)
        led.value(0)
        utime.sleep(0.2)  # Inter-character pause

def blink_word(word):
    for char in word:
        blink_morse(char)
        utime.sleep(0.6)  # Inter-word pause


message = "Hello world."  # Example message

# Repeat the message indefinitely
while True:
    blink_word(message)
    utime.sleep(2)  # Pause between repetitions (adjust as needed)

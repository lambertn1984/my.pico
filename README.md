# my.pico

Repository for the `pico 2 W` programs.

## Run a script on the Pico

There are two method

1. Run from the terminal (simpler)

    This is to test a script when connected to a PC. It will continue when plug & unplug. 

        ampy --port /dev/ttyACM0 run [my.code.py]

    Reset to stop he script 
    
        ampy --port /dev/ttyACM0 reset

    Copy a file to the board 

        ampy --port /dev/ttyACM0 put [my.script.ph] main.py

1. Export script to the pico (useful when adding more than one script)

    Plug the Pico and do not open Thonny. Connect to the Pico with `rshell`. 

        rshell -p /dev/ttyACM0 --buffer-size 512

    Copy the script to `/main.py/` (with `/` at the end).

        cp [my.code.py] /main.py/

    Disconnect 

        exit 




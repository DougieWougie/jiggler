'''
Here be sharks...

Remember this disables identifying as USB or REPL so it works on locked down devices (assuming the allow HID). Touching either button on boot will stop it!

More here https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#dont-lock-yourself-out-3096636-14
'''

import storage
import usb_cdc
import board
import touchio

left = touchio.TouchIn(board.TOUCH1)
right = touchio.TouchIn(board.TOUCH2)

def disable():
    storage.disable_usb_drive()    # Disable USB storage
    usb_cdc.disable()              # Disable REPL

if not left.value:
    disable()
elif not right.value:
    disable()

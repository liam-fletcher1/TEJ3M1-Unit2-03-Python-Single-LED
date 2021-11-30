# !/usr/bin/env python3
#
# Created by: Liam Fletcher
# Created on: Nov 2021
# This will display the LED over an interval of 1 second
#  and increase by 1 second more every on and off cycle 

import time
import board
import digitalio

# variable is set to a value of 1000 milliseconds 
blink_time = 1.0 

# external LED is connected to pin 13 on the Pico
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

while True: 
    led.value = True
    # while the LED is on, keep it on by the value of the variable
    time.sleep(blink_time) 
    led.value = False
    # while the LED is off, wait for a second
    time.sleep(1.0)  

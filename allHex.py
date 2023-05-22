# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio
from ledPixelsPico import *

touch_pad7 = board.GP18
ledPix7 = ledPixels(24, board.GP22)

touch_pad6 = board.GP9
ledPix6 = ledPixels(24, board.GP11)

touch_pad5 = board.GP14
ledPix5 = ledPixels(24, board.GP12)

touch_pad4 = board.GP5 
ledPix4 = ledPixels(24, board.GP4)

touch_pad3 = board.GP13 
ledPix3 = ledPixels(24, board.GP2)

touch_pad2 = board.GP3 
ledPix2 = ledPixels(24, board.GP1)


touch_pad = board.GP17  # Will not work for Circuit Playground Express!
# touch_pad = board.A1  # For Circuit Playground Express
ledPix = ledPixels(24, board.GP0)




ledPix.clear()
ledPix2.clear()
ledPix3.clear()
ledPix4.clear()
ledPix5.clear()
ledPix6.clear()
ledPix7.clear()

print("hello")      
                    
touch = touchio.TouchIn(touch_pad)
touch2 = touchio.TouchIn(touch_pad2)
touch3 = touchio.TouchIn(touch_pad3)
touch4 = touchio.TouchIn(touch_pad4)
touch5 = touchio.TouchIn(touch_pad5)
touch6 = touchio.TouchIn(touch_pad6)
touch7 = touchio.TouchIn(touch_pad7)

n = 0

while True:
    if touch.value:
 #       ledPix.rainbow(speed=0.005)
        ledPix.setColor([0,0,50])
    else:
        ledPix.clear()
        
    if touch2.value:
        ledPix2.setColor([0,0,50])
    else:
        ledPix2.clear()
        
    if touch3.value:
        ledPix3.setColor([0,0,50])
    else:
        ledPix3.clear()
        
    if touch4.value:
        ledPix4.setColor([0,0,50])
    else:
        ledPix4.clear()
        
    if touch5.value:
        ledPix5.setColor([0,0,50])
    else:
        ledPix5.clear()
        
    if touch6.value:
        ledPix6.setColor([0,0,50])
    else:
        ledPix6.clear()
        
    if touch7.value:
        ledPix7.setColor([0,0,50])
    else:
        ledPix7.clear()
        
        
        






# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio
from ledPixelsPico import *


class hexFunc:
    def __init__(self, tGP = board.GP18, lGP = board.GP22,  color = [0,0,50]):
        self.tGP = tGP
        self.lGP = lGP
        self.ledPix = ledPixels(24, lGP)
        self.ledPix.clear()
        self.touch = touchio.TouchIn(tGP)
        self.color = color
        
    def Hexagon(self):
        if self.touch.value:
            self.ledPix.setColor(self.color)
        else:
            self.ledPix.clear()

hexs = []
hexs.append(hexFunc(color = [0,50,0]))
hexs.append(hexFunc(board.GP9, board.GP11))
hexs.append(hexFunc(board.GP14, board.GP12))
hexs.append(hexFunc(board.GP5, board.GP4))
hexs.append(hexFunc(board.GP13, board.GP2))
hexs.append(hexFunc(board.GP3, board.GP1))
hexs.append(hexFunc(board.GP17, board.GP0, [50,0,0]))



while True:
    for i in hexs:
        i.Hexagon()




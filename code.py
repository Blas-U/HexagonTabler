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
# hexs.append(hexFunc(color = [0,50,0]))
hexs.append(hexFunc(board.GP2, board.GP3, [50,0,0]))
hexs.append(hexFunc(board.GP10, board.GP11))
hexs.append(hexFunc(board.GP12, board.GP13))
hexs.append(hexFunc(board.GP16, board.GP17))
hexs.append(hexFunc(board.GP18, board.GP19))
hexs.append(hexFunc(board.GP20, board.GP21, [50,0,0]))
# control hex
hexs.append(hexFunc(board.GP14, board.GP15))



while True:
    for hex in hexs[:-1]:
        #i.Hexagon()
        if hex.touch.value:
            hex.ledPix.setColor(hex.color)
        else:
            hex.ledPix.clear()
    if hexs[-1].touch.value:
        for hex in hexs[:-1]:
            hex.ledPix.setColor(hex.color)
        while hexs[-1].touch.value:
            pass
        for hex in hexs[:-1]:
            hex.ledPix.clear()




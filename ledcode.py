import board
import neopixel

pixels = neopixel.NeoPixel(board.GP0, 12)

pixels[0] = (20,0,0)
pixels[-1] = (0,20,0)
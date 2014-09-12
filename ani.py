#!/usr/bin/python
#===============================================================================
# ani.py
#
# low level writes to test animation
#===============================================================================
import time
import random
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight

matrix = []
matrix.append(EightByEight(address=0x70))
matrix.append(EightByEight(address=0x71))
matrix.append(EightByEight(address=0x72))
matrix.append(EightByEight(address=0x73))

matrix[0].disp.setBrightness(1)
matrix[1].disp.setBrightness(1)
matrix[2].disp.setBrightness(1)
matrix[3].disp.setBrightness(1)

#---------------------
#---------------------
def set_led(bitmap,i):
  for x in xrange(8):
    for y in xrange(8):
      matrix[i].setPixel(x, y, bitmap[y][x])
   
#---------------------
#---------------------
while(True):
  for i in xrange(8):
    for n in xrange(4):
      matrix[n].disp.setBufferRow(i,random.randrange(256))
  for n in xrange(4):
    matrix[n].disp.writeDisplay()
  time.sleep(1.0)

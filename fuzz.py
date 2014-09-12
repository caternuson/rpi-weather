#!/usr/bin/python
#===============================================================================
# fuzz.py
#
# create random patterns on 8x8s
#===============================================================================
import time
import random
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight

matrix = []
matrix.append(EightByEight(address=0x70))
matrix.append(EightByEight(address=0x71))
matrix.append(EightByEight(address=0x72))
matrix.append(EightByEight(address=0x73))

while True:
  for i in xrange(4):
    for x in xrange(8):
      for y in xrange(8):
        matrix[i].setPixel(x,y, random.randrange(0,2))
  time.sleep(1)

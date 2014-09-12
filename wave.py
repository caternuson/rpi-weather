#!/usr/bin/python
#===============================================================================
# wave.py
#
# kind of a sine wave pattern thing
#===============================================================================
import time
import math
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight

matrix = []
matrix.append(EightByEight(address=0x70))
matrix.append(EightByEight(address=0x71))
matrix.append(EightByEight(address=0x72))
matrix.append(EightByEight(address=0x73))

matrix[0].disp.setBrightness(15)
matrix[1].disp.setBrightness(15)
matrix[2].disp.setBrightness(15)
matrix[3].disp.setBrightness(15)


def plot(x,y):
  if x<0 or x>64:
    return 
  if y<0 or y>8:
    return
  if x<8:
    i = 0
  elif x<16:
    i = 1
  elif x<24:
    i = 2
  elif x<32:
    i = 3
  row = x - i*8
  for j in xrange(8):
    matrix[i].setPixel(int(row),j,0)
  #matrix[i].writeRowRaw(int(row), 0)
  #print int(xx),int(y)
  matrix[i].setPixel(int(row),int(y),1)

pi = 0;
while True:
  for i in xrange(32):
    g = 4 + 4*math.sin(pi + i*6.28/32.0)
    plot(i,g)
  pi = pi + 6.28/32.0
  if pi>6.28:
    pi = 0

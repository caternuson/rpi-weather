#!/usr/bin/python
#===============================================================================
# icon_test.py
#
# simply loads and displays icons
#===============================================================================
import sys
import httplib
import time
from xml.dom.minidom import parseString
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight
from LED8x8_Icons import Icons as ICONS

matrix = []
matrix.append(EightByEight(address=0x70))
matrix.append(EightByEight(address=0x71))
matrix.append(EightByEight(address=0x72))
matrix.append(EightByEight(address=0x73))


#---------------------
#---------------------
def set_led(bitmap,i):
  for x in xrange(8):
    for y in xrange(8):
      matrix[i].setPixel(x, y, bitmap[y][x])

set_led(ICONS.SUNNY,0)
set_led(ICONS.RAIN,1)
set_led(ICONS.CLOUD,2)
set_led(ICONS.SHOWERS,3)
#set_led(ICONS.UNKNOWN,i)

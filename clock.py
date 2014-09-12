#!/usr/bin/python
#===============================================================================
# clock.py
#
# simple clock interface
#===============================================================================
import time
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight
from LED8x8_Digits import Digits as DIGIT 

matrix = []
matrix.append(EightByEight(address=0x70))
matrix.append(EightByEight(address=0x71))
matrix.append(EightByEight(address=0x72))
matrix.append(EightByEight(address=0x73))

matrix[0].disp.setBrightness(15)
matrix[1].disp.setBrightness(15)
matrix[2].disp.setBrightness(15)
matrix[3].disp.setBrightness(15)

#---------------------
#---------------------
def set_led(bitmap,i):
  for x in xrange(8):
    for y in xrange(8):
      matrix[i].setPixel(x, y, bitmap[y][x])
   
#---------------------
#---------------------
def disp_num(number):
  num = int(number)
  if num>9999 or num<0:
    return
  if num<1000:
    matrix[0].clear()
  i = 3
  while num:
    digit = num % 10
    if digit==0:
      set_led(DIGIT.ZERO,i)
    if digit==1:
      set_led(DIGIT.ONE,i)
    if digit==2:
      set_led(DIGIT.TWO,i)
    if digit==3:
      set_led(DIGIT.THREE,i)
    if digit==4:
      set_led(DIGIT.FOUR,i)
    if digit==5:
      set_led(DIGIT.FIVE,i)
    if digit==6:
      set_led(DIGIT.SIX,i)
    if digit==7:
      set_led(DIGIT.SEVEN,i)
    if digit==8:
      set_led(DIGIT.EIGHT,i)
    if digit==9:
      set_led(DIGIT.NINE,i)
    num /= 10
    i -= 1

#---------------------
#---------------------
while(True):
  hour = time.localtime().tm_hour
  if hour>12:
    hour -= 12 
  val = hour * 100
  val += time.localtime().tm_min
  disp_num(val)
  time.sleep(1)

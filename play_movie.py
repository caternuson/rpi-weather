#!/usr/bin/python
#===============================================================================
# play_movie.py
#
# play "movies"
#===============================================================================
import time
import sys
import pickle
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

#-----------------------
#-----------------------
def binarify(val):
  b = [0,]*8
  d = 0
  while val:
    b[d] = val&1
    val >>= 1
    d += 1
  return b

#-----------------------
#-----------------------
def digify(b):
  n = 0
  val = 0
  for d in b:
    val += d*(2**n)
    n += 1
  return val

#-----------------------
#-----------------------
def fix_val(val):
  b1 = binarify(val)
  #b2 = b1[7:] + b1[:7]
  b2 = b1[1:] + b1[:1]
  return digify(b2)

#---------------------
#---------------------
def set_bitmap(bitmap,led):
  for row in xrange(8):
    rowVal = fix_val(bitmap[row])
    matrix[led].disp.setBufferRow(row,rowVal,False)
  matrix[led].disp.writeDisplay()
 
#---------------------
#---------------------
def play_frames(frames, delay=1, led=0, repeat=5):
  while repeat!=0:
    print repeat
    for frame in frames:
      #print frame
      set_bitmap(frame, led)
      time.sleep(delay)
    repeat -= 1
    

#---------------------
#---------------------
def play_movie(movie, leds):
  repeat = 5
#  while repeat>0:
  while True:
    for frame in movie:
      bitmap = frame[0]
      delay = frame[1]
      for led in leds:
        set_bitmap(bitmap, led)
      #time.sleep(delay)
      time.sleep(0.05)
#    repeat -= 1

#---------------------
#---------------------
if len(sys.argv)<2:
  exit()
movie = pickle.load(open(sys.argv[1],'r'))
leds = xrange(4)
if len(sys.argv)>2:
  leds = eval(sys.argv[2])
play_movie(movie,leds)


#!/usr/bin/python
#===============================================================================
# ani2.py
#
# play "movies"
#===============================================================================
import time
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

#---------------------
#---------------------
def set_bitmap(bitmap,led):
  for row in xrange(8):
    matrix[led].disp.setBufferRow(row,bitmap[row],False)
  matrix[led].disp.writeDisplay()
 
#---------------------
#---------------------
def play_frames(frames, delay=1, led=0, repeat=1):
  for frame in frames:
    #print frame
    set_bitmap(frame, led)
    time.sleep(delay)

#---------------------
#---------------------
frames=[]
with open('sunrise.mv','r') as f:
  for line in f:
    #print line
    frames += eval(line)
play_frames(frames,0.2,0)
play_frames(frames,0.2,1)
play_frames(frames,0.2,2)
play_frames(frames,0.2,3)

#!/usr/bin/python
#-----------------------------------------------------------
# press a button, random stuff on 8x8 led
#
#-----------------------------------------------------------
import time
import datetime
import random 
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

grid = EightByEight(address=0x70)

print "Press CTRL+Z to exit"

bitmap = [\
 [0, 1, 0, 1, 0, 1, 0, 1], \
 [1, 0, 1, 0, 1, 0, 1, 0], \
 [0, 1, 0, 1, 0, 1, 0, 1], \
 [1, 0, 1, 0, 1, 0, 1, 0], \
 [0, 1, 0, 1, 0, 1, 0, 1], \
 [1, 0, 1, 0, 1, 0, 1, 0], \
 [0, 1, 0, 1, 0, 1, 0, 1], \
 [1, 0, 1, 0, 1, 0, 1, 0], \
]

#----------------------
# random 8x8 display
#----------------------
def rand_disp8x8():
  for x in range(0, 8):
    for y in range(0, 8):
      grid.setPixel(x, y, random.randint(0,1))

def display(bm):
  for x in range(0, 8):
    for y in range(0, 8):
     grid.setPixel(x, y, bm[x][y])

#----------------------
# Setup the input pin
#----------------------
BUTTON_PIN = 23
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#----------------------
# Go
#----------------------
DOWN = GPIO.LOW
UP = GPIO.HIGH
last_state = GPIO.input(BUTTON_PIN)
ready_to_fire = False
while True:
    current_state = GPIO.input(BUTTON_PIN) 
    if current_state==UP:
       ready_to_fire = True
       continue
    if ready_to_fire:
       print "BANG"
       #rand_disp8x8()
       display(bitmap)
       ready_to_fire=False
       time.sleep(0.05)          # mitigate button bounce
 

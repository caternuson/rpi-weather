#!/usr/bin/python
#===============================================================================
# clock.py
#
# Simple clock interface for four 8x8 LED display.
#
# 2014-09-12
# Carter Nelson
#===============================================================================
import rpi_weather
from led8x8icons import LED8x8_ICONS
import time

display = rpi_weather.RpiWeather()
   
#---------------------
#---------------------
while(True):
    hour = time.localtime().tm_hour
    if hour>12:
        hour -= 12 
    val = hour * 100
    val += time.localtime().tm_min
    display.disp_num(val)
    time.sleep(10)

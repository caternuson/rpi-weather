#===============================================================================
# clock.py
#
# Simple clock interface for four 8x8 LED display.
#
# 2014-09-12
# Carter Nelson
#===============================================================================
import time
from rpi_weather import RpiWeather
from led8x8icons import LED8x8_ICONS

display = RpiWeather()

old_val = 0
   
while True:
    hour = time.localtime().tm_hour
    if hour>12:
        hour -= 12 
    val = hour * 100
    val += time.localtime().tm_min
    if val != old_val :
      old_val = val
      display.disp_number(val)
    time.sleep(10)

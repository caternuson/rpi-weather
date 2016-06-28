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

display = RpiWeather()

old_val = 0
   
while True:
    """Loop forever, updating every 10 seconds."""
    hour = time.localtime().tm_hour
    if hour>12:
        hour -= 12 
    val = hour * 100
    val += time.localtime().tm_min
    if val != old_val :
      old_val = val
      display.disp_number(val)
    time.sleep(10)

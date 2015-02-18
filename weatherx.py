#!/usr/bin/python
#===============================================================================
# weatherx.py
#
# Get weather forecast from NOAA and turn it into "icons"
#   * Kind of tailored to work with 12-hour format
#   * NOAA's doc: http://graphical.weather.gov/xml/rest.php
#   * Set location with LAT and LON (negative LON for west)
#   * Somewhat generalized for any number of days
#
#===============================================================================
import sys
import httplib
import time
from xml.dom.minidom import parseString
from Adafruit_LED_Backpack import Matrix8x8
from led8x8icons import LED8x8_ICONS

matrix = []
matrix.append(Matrix8x8.Matrix8x8(address=0x70, busnum=1))
matrix.append(Matrix8x8.Matrix8x8(address=0x71, busnum=1))
matrix.append(Matrix8x8.Matrix8x8(address=0x72, busnum=1))
matrix.append(Matrix8x8.Matrix8x8(address=0x73, busnum=1))
for m in matrix:
  m.begin()

#------------------------------------
# do this if anything bad happens
#------------------------------------
def giveup():
  for i in xrange(4):
    set_led(LED8x8_ICONS['UNKNOWN'],i)
  print "something happened...giving up...."
  sys.exit(1)

#------------------------------------
# set up
#------------------------------------
NOAA_URL    = "graphical.weather.gov"
REQ_BASE    = r"/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?"
LAT         = 47.54583
LON         = -122.31361
TIME_FORMAT = "12+hourly"
NUM_DAYS    = 4
REQUEST = REQ_BASE + "lat={0}&".format(LAT)+\
                     "lon={0}&".format(LON)+\
                     "format={0}&".format(TIME_FORMAT)+\
                     "numDays={0}".format(NUM_DAYS)

#------------------------------------
# set 8x8 matrix based on bitmap
#------------------------------------
def set_led(bitmap,i):
  for x in xrange(8):
    for y in xrange(8):
      matrix[i].set_pixel(x, y, bitmap[y][x])
  matrix[i].write_display()

#------------------------------------
# set 8x8 matrix based on 64 bit value
#------------------------------------    
def set_raw64(value, i):
  matrix[i].clear()
  for y in [0, 1, 2, 3, 4, 5, 6, 7]:
    row_byte = value>>(8*y)
    for x in [0, 1, 2, 3, 4, 5, 6, 7]:
      pixel_bit = row_byte>>x&1 
      matrix[i].set_pixel(x,y,pixel_bit) 
  matrix[i].write_display()
  
#------------------------------------
# make the request
#------------------------------------
try:
  conn = httplib.HTTPConnection(NOAA_URL)
  conn.request("GET", REQUEST)
  resp = conn.getresponse()
  data = resp.read()
except:
  giveup()

#filename = time.strftime('%y%m%d_%H%M')+"_weather.log"
#with open(filename,"w") as FILE:
#  FILE.write("-"*80+"\n")
#  FILE.write("URL = " + NOAA_URL + "\n")
#  FILE.write("REQUEST = " + REQUEST + "\n")
#  FILE.write("-"*80+"\n")
#  FILE.write(data)

#------------------------------------
# parse the XML response into the DOM
#------------------------------------
dom = parseString(data)

#------------------------------------
# get the weather summay elements
#------------------------------------
vals = dom.getElementsByTagName("weather-conditions")
if len(vals)<2*NUM_DAYS:
    print "Wrong stuff: len = %d   NUM_DAYS = %d" % (len(vals), NUM_DAYS)
    giveup()

#------------------------------------
# The first entry may be for the current day, or current night
# I'll try and fix that using local time.
# Then I want every other entry for the daytime forecast
#------------------------------------
offset = 0
if time.localtime().tm_hour > 12:
   offset = 1
forecast = [e.getAttribute("weather-summary") for e in vals[offset::2]]
#print forecast

#------------------------------------
# print results
#------------------------------------
print '-'*20
print time.strftime('%Y/%m/%d %H:%M:%S')
print '-'*20
for day in forecast:
    print day

#------------------------------------
# set matrix icons based on forecast text
#------------------------------------
for i in xrange(4):
  if "SUNNY" in forecast[i].encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['SUNNY'], i)
  elif "RAIN" in forecast[i].encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['RAIN'], i)
  elif "CLOUD" in forecast[i].encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['CLOUD'], i)
  elif "SHOWERS" in forecast[i].encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['SHOWERS'], i)
  else:
    set_raw64(LED8x8_ICONS['UNKNOWN'], i)

#===============================================================================
# weatherx.py
#
# Get weather forecast from NOAA and turn it into "icons"
#   * Tailored to work with 12-hour format
#   * NOAA's doc: http://graphical.weather.gov/xml/rest.php
#   * Set location using zipcode
#   * Somewhat generalized for any number of days
#
# 2014-09-14
# Carter Nelson
#===============================================================================
import time
import httplib
import sys
from xml.dom.minidom import parseString

from rpi_weather import RpiWeather
from led8x8icons import LED8x8_ICONS

display = RpiWeather()

#------------------------------------
# set up
#------------------------------------
NOAA_URL    = "graphical.weather.gov"
REQ_BASE    = r"/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?"
TIME_FORMAT = "12+hourly"
NUM_DAYS    = 4
ZIPCODE     = 98109
REQUEST = REQ_BASE + "zipCodeList={0}&".format(ZIPCODE)+\
                     "format={0}&".format(TIME_FORMAT)+\
                     "numDays={0}".format(NUM_DAYS)

#------------------------------------
# do this if anything bad happens
#------------------------------------
def giveup():
    for matrix in xrange(4):
        display.set_raw64(LED8x8_ICONS['UNKNOWN'],matrix)
    print "something happened...giving up...."
    sys.exit(1)
    
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
# get forecast
#------------------------------------
offset = 0
if time.localtime().tm_hour < 6:
    offset = 1
forecast = [e.getAttribute("weather-summary") for e in vals[offset::2]]

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
        display.set_raw64(LED8x8_ICONS['SUNNY'], i)
    elif "RAIN" in forecast[i].encode('ascii','ignore').upper():
        display.set_raw64(LED8x8_ICONS['RAIN'], i)
    elif "CLOUD" in forecast[i].encode('ascii','ignore').upper():
        display.set_raw64(LED8x8_ICONS['CLOUD'], i)
    elif "SHOWERS" in forecast[i].encode('ascii','ignore').upper():
        display.set_raw64(LED8x8_ICONS['SHOWERS'], i)
    else:
        display.set_raw64(LED8x8_ICONS['UNKNOWN'], i)

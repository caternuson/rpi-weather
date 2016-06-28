# rpi-weather
![thumbnail](http://caternuson.github.io/rpi-weather/rpi-weather-thumb.jpg)<br/>
Python 2.7 application to get local weather forecast and display results
via icons on LED 8x8 matrices.

# Hardware
This program should work with any Raspberry Pi although I have only tested it
with an original Model A (yes, an A). Also, any 4 Adafruit 8x8 LED
Matrices with I2C Backpacks should work. Be sure to solder the address jumpers
to set unique addresses for each. Expected range is 0x70-0x73.

# Software
A brief description of the various software components.
* ```weather.py``` - gets and displays forecast
* ```rpi_weather.py``` - defines a class for interfacing with the hardware
* ```led8x8icons.py``` - contains a dictionary of icons
* ```clock.py``` - displays the time, for use as a clock

# Dependencies
*  Adafruit Python Library for LED Backpacks
    * https://github.com/adafruit/Adafruit_Python_LED_Backpack

# Install
Simply clone this repo and run:
```
$ git clone https://github.com/caternuson/rpi-weather.git
$ cd rpi-weather
$ sudo python weather.py
```

# Configure
The forecast location is specified with a zipcode. A default zipcode can be
set in the code:
```python
ZIPCODE = 98109
```
A zipcode can also be passed in from the command line, which will override the
default:
```
$ sudo python weather.py 98109
```

# Automation
The easiest way to have the program run on a daily basis is to use ```cron```.
Use ```crontab -e``` to add the following entry, which will run the program
every morning at 4AM:
```
0 4 * * * sudo -E PYTHONPATH=$PYTHONPATH python /home/pi/rpi-weather/weather.py
```
**NOTE:** If you installed the program in a different location, change the path
accordingly.

# NOAA REST
The forecast is determined using the [NOAA REST](http://graphical.weather.gov/xml/rest.php)
web service. Specifically, the **Summarized Data for One or More Zipcodes**. A
typical request looks like:
```
http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?zipCodeList=98109&format=12+hourly&numDays=4
```
The key bits being:
* ```zipCodeList``` - zipcode(s) for forecast
* ```format``` - choose either 12 or 24 hour period
* ```numDays``` - number of days in forecast

The request returns XML data. The icons are set by a simple text search in the
```weather-summary``` attribute of the ```weather-conditions``` tag.

# Icons
| Show this icon | If weather-summary contains  |
| :---: | :---: |
| ![SUNNY](https://github.com/caternuson/rpi-weather/blob/gh-pages/SUNNY.jpg) | SUNNY |
| ![RAIN](https://github.com/caternuson/rpi-weather/blob/gh-pages/RAIN.jpg) | RAIN |
| ![CLOUD](https://github.com/caternuson/rpi-weather/blob/gh-pages/CLOUD.jpg) | CLOUD |
| ![SHOWERS](https://github.com/caternuson/rpi-weather/blob/gh-pages/SHOWERS.jpg) | SHOWERS |
| ![STORM](https://github.com/caternuson/rpi-weather/blob/gh-pages/STORM.jpg) | STORM |
| ![SNOW](https://github.com/caternuson/rpi-weather/blob/gh-pages/SNOW.jpg) | SNOW |
| ![UNKNOWN](https://github.com/caternuson/rpi-weather/blob/gh-pages/UNKNOWN.jpg) | none of the above |

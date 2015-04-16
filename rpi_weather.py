#!/usr/bin/python
#===============================================================================
# rpi-weather.py
#
# Class for interfacing to Raspberry Pi with four Adafruit 8x8 LEDs attached.
#
# 2015-04-15
# Carter Nelson
#===============================================================================
from Adafruit_LED_Backpack import Matrix8x8
from led8x8icons import LED8x8_ICONS

class RpiWeather():
    
    def __init__(self, ):
        self.matrix = []
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x70, busnum=1))
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x71, busnum=1))
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x72, busnum=1))
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x73, busnum=1))
        for m in self.matrix:
          m.begin()
          
    def clear_disp(self, ):
        for m in self.matrix:
            m.clear()
          
    def set_led(self, bitmap, i):
        for x in xrange(8):
            for y in xrange(8):
                self.matrix[i].set_pixel(x, y, bitmap[y][x])
        self.matrix[i].write_display()
      
    def set_raw64(self, value, i):
        self.matrix[i].clear()
        for y in [0, 1, 2, 3, 4, 5, 6, 7]:
            row_byte = value>>(8*y)
            for x in [0, 1, 2, 3, 4, 5, 6, 7]:
                pixel_bit = row_byte>>x&1 
                self.matrix[i].set_pixel(x,y,pixel_bit) 
        self.matrix[i].write_display()
        
    def disp_num(self, number):    
        num = int(number)
        if num>9999 or num<0:
            return
        self.clear_disp()
        i = 3
        while num:
            digit = num % 10
            self.set_raw64(LED8x8_ICONS['%1i'%digit], i)
            num /= 10
            i -= 1
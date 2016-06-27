#===============================================================================
# led8x8icons.py
#
# Dictionary of LED 8x8 matrix icons as 64 bit values.
#
# Code snippet for computing value from bitmap:
#
#           BITMAP = [
#           [1, 1, 1, 1, 1, 1, 1, 1,],
#           [1, 1, 0, 0, 0, 0, 0, 1,],
#           [1, 0, 1, 0, 0, 0, 0, 1,],
#           [1, 0, 0, 1, 0, 0, 0, 1,],
#           [1, 0, 0, 0, 1, 0, 0, 1,],
#           [1, 0, 0, 0, 0, 1, 0, 1,],
#           [1, 0, 0, 0, 0, 0, 1, 1,],
#           [1, 0, 0, 0, 0, 0, 0, 1,],
#           ]
#           value = 0
#           for y,row in enumerate(BITMAP):
#               row_byte = 0
#               for x,bit in enumerate(row):
#                   row_byte += bit<<x    
#               value += row_byte<<(8*y)
#           print '0x'+format(value,'02x')
#
# Code snippet for setting individual LEDs on the display.
#
#        def set_raw64(value):
#            led8x8matrix.clear()
#            for y in xrange(8):
#                row_byte = value>>(8*y)
#                for x in xrange(8):
#                    pixel_bit = row_byte>>x&1 
#                    led8x8matrix.set_pixel(x,y,pixel_bit) 
#            led8x8mmatrix.write_display() 
#
# 2014-10-20
# Carter Nelson
#==============================================================================
LED8x8_ICONS = { 
#---------------------------------------------------------
# misc
#---------------------------------------------------------
'ALL_ON'                            : 0xffffffffffffffff ,
'ALL_OFF'                           : 0x0000000000000000 ,
'UNKNOWN'                           : 0x00004438006c6c00 ,
'BOTTOM_ROW'                        : 0xff00000000000000 ,
'TOP_ROW'                           : 0x00000000000000ff , 
'LEFT_COL'                          : 0x0101010101010101 ,
'RIGHT_COL'                         : 0x8080808080808080 ,
'BOX'                               : 0xff818181818181ff ,
'XBOX'                              : 0xffc3a59999a5c3ff ,
#---------------------------------------------------------
# weather
#---------------------------------------------------------
'SUNNY'                             : 0x9142183dbc184289 ,
'RAIN'                              : 0x55aa55aa55aa55aa ,
'CLOUD'                             : 0x00007e818999710e ,
'SHOWERS'                           : 0x152a7e818191710e ,
'SNOW'                              : 0xa542a51818a542a5 ,
#---------------------------------------------------------
# digits
#---------------------------------------------------------
'0'                                 : 0x003c42464a52623c ,
'1'                                 : 0x003e0808080e0808 ,
'2'                                 : 0x007e02023c40403e ,
'3'                                 : 0x003e40403040403e ,
'4'                                 : 0x004040407e424242 ,
'5'                                 : 0x003e40403e02027e ,
'6'                                 : 0x003c42423e02027c ,
'7'                                 : 0x004040404042427e ,
'8'                                 : 0x003c42423c42423c , 
'9'                                 : 0x003c40407c42423c ,
#---------------------------------------------------------
# default
#---------------------------------------------------------
''                                  : 0x0000000000000000 ,
}
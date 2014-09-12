#===============================================================================
# tk8x8.py
#
# Uses Python Tkinter GUI modules to provide interaction with the Adafruit
# 8x8 LED matrix.
#===============================================================================
from Tkinter import *
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight

grid = EightByEight(address=0x73)

# define grid size
NX = 8
NY = 8

#-----------------------------------------
# the Tkinter App class
#-----------------------------------------
class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.vars =[[IntVar() for x in xrange(NX)] for y in xrange(NY)]

        #-------
        # set up checkbuttons
        #-------
        self.checks = [[0 for x in xrange(NX)] for y in xrange(NY)]
        for x in xrange(NX):
            for y in xrange(NY):
                self.checks[x][y] = \
        Checkbutton(frame, text="", variable=self.vars[x][y], command=self.display)

        for x in xrange(NX):
            for y in xrange(NY):
                self.checks[x][y].grid(row=x,column=y)

        #-----------
        # buttons
        #-----------
        self.b1 = Button(frame, text="CLEAR", command=self.clear_all)
        self.b1.grid(row=NX+1,column=1,columnspan=NX)
 
        self.b2 = Button(frame, text="SAVE", command=self.save_it)
        self.b2.grid(row=NX+2,column=1,columnspan=NX)
 
        self.b3 = Button(frame, text="SAVE BM", command=self.save_bitmap)
        self.b3.grid(row=NX+3,column=1,columnspan=NX)

    def report(self):
        print "-"*17
        for x in range(8):
         print "",
         for y in range(8):
          print self.vars[x][y].get(),
         print
        print "-"*17

    #------------------------
    # display current results on grid
    #-----------------------
    def display(self):
        for x in range(0, 8):
          for y in range(0, 8):
            grid.setPixel(x, y, self.vars[y][x].get())

    #-----------------------
    # clear it all
    #-----------------------
    def clear_all(self):
        for x in range(0, 8):
          for y in range(0, 8):
           self.vars[x][y].set(0),
        self.display()

    #-----------------------
    # save it
    #-----------------------
    def save_it(self):
        with open("led.out","w") as FILE:
          for x in range(0, 8):
            for y in range(0, 8):
              FILE.write("{0}, ".format(self.vars[x][y].get()))
            FILE.write("\n")

    #-----------------------
    # save bitmap
    #-----------------------
    def save_bitmap(self):
        with open("bitmap.out","w") as FILE:
           FILE.write("{0}\n".format(grid.disp.getBuffer()))
          
#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
root = Tk()
app = App(root)
root.mainloop()

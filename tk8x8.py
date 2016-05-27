#===============================================================================
# tk8x8.py
#
# Uses Python Tkinter GUI modules to provide interaction with the Adafruit
# 8x8 LED matrix.
#
# 2016-05-26
# Carter Nelson
#===============================================================================
from Tkinter import *
from Adafruit_LED_Backpack import Matrix8x8

matrix = Matrix8x8.Matrix8x8(address=0x70)

# define grid size
NX = 8
NY = 8

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.vars =[[IntVar() for x in xrange(NX)] for y in xrange(NY)]

        self.checks = [[0 for x in xrange(NX)] for y in xrange(NY)]
        for x in xrange(NX):
            for y in xrange(NY):
                self.checks[x][y] = Checkbutton(frame, text="", variable=self.vars[x][y], command=self.display)

        for x in xrange(NX):
            for y in xrange(NY):
                self.checks[x][y].grid(row=x,column=y)

        self.b1 = Button(frame, text="CLEAR", command=self.clear_all)
        self.b1.grid(row=NX+1,column=0,columnspan=4)
 
        self.b2 = Button(frame, text="SAVE", command=self.save_it)
        self.b2.grid(row=NX+1,column=4,columnspan=4)
        
        self.tx_raw64 = Text(frame,width=18, height=1)
        self.tx_raw64.grid(row=NX+3,column=0,columnspan=NX)
        self.tx_raw64.insert("1.0","0x0000000000000000")

    def report(self):
        """ Print current results to display. """
        print "-"*17
        for x in xrange(8):
            print "",
            for y in xrange(8):
                print self.vars[x][y].get(),
            print
        print "-"*17

    def display(self):
        """ Display current results. """
        value = 0
        for y in xrange(8):
            row_byte = 0
            for x in xrange(8):
                bit = self.vars[y][x].get()
                row_byte += bit<<x 
                matrix.set_pixel(x, y, bit)
            value += row_byte<<(8*y)    
        matrix.write_display()
        self.tx_raw64.delete("1.0",END)
        self.tx_raw64.insert("1.0",'0x'+format(value,'016x'))

    def clear_all(self):
        """ Clear the display. """
        for x in range(0, 8):
            for y in range(0, 8):
                self.vars[x][y].set(0),
        self.display()

    def save_it(self):
        """ Save current settings to a text file. """ 
        with open("led.out","w") as FILE:
            for x in range(0, 8):
                for y in range(0, 8):
                    FILE.write("{0}, ".format(self.vars[x][y].get()))
                FILE.write("\n")
                
#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
root = Tk()
app = App(root)
root.mainloop()

#===============================================================================
# movie_maker.py
#
# Makes "movies" for 8x8 LED. 
#
# rowVal = 8bit value for row:
#             0=all off, 255=all on
# bitmap = list of 8bit vaues for each row:
#             [r0,r1,r2,r3,r4,r5,r6,r7] 
# frame = [bitmap, dt], where dt is pause time to next frame
# movie = list of frames [f0, f1..fN]
#
# The movie object is saved with pickle module streaming.
#
# Uses Python Tkinter GUI modules to provide interaction with the Adafruit
# 8x8 LED matrix.
#===============================================================================
import pickle
import copy
from Tkinter import *
from Adafruit_Raspberry_Pi_Python_Code.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight

led8x8 = EightByEight(address=0x70)


#-----------------------------------------
# the Tkinter App class
#-----------------------------------------
class App:

  DEFAULT_DT = 0.5
  DEFAULT_BITMAP = [0,]*8
  DEFAULT_FRAME = [DEFAULT_BITMAP,DEFAULT_DT]
  movie = []
  currentFrame = 0
  NX = 8
  NY = 8
  vars =[]
  checks = []

  #--------------------------------------
  # CTOR
  #--------------------------------------
  def __init__(s, master):

    frame = Frame(master)
    frame.pack()

    s.vars =[[IntVar() for x in xrange(s.NX)] for y in xrange(s.NY)]
    s.checks = [[0 for x in xrange(s.NX)] for y in xrange(s.NY)]

    s.movie.append(copy.copy(s.DEFAULT_FRAME))

    #-------
    # set up checkbuttons
    #-------
    for x in xrange(s.NX):
      for y in xrange(s.NY):
        s.checks[x][y] = Checkbutton(frame, text="", variable=s.vars[x][y], command=s.display)

    for x in xrange(s.NX):
      for y in xrange(s.NY):
        s.checks[x][y].grid(row=x,column=y)

    #-----------
    # buttons
    #-----------
    s.b1 = Button(frame, text="CLEAR", command=s.clear_all)
    s.b1.grid(row=s.NX+1,column=0,columnspan=4)

    s.b2 = Button(frame, text="SAVE", command=s.save_movie)
    s.b2.grid(row=s.NX+1,column=4,columnspan=4)

    s.bPrevFrame = Button(frame, text="<<", command=s.prev_frame)
    s.bPrevFrame.grid(row=s.NX+2,column=0,columnspan=4)

    s.bNextFrame = Button(frame, text=">>", command=s.next_frame)
    s.bNextFrame.grid(row=s.NX+2,column=4,columnspan=4)

  #------------------------
  # why is this here?
  #-----------------------
  def report(self):
    print "-"*17
    for x in xrange(8):
      print "",
      for y in xrange(8):
        print self.vars[x][y].get(),
      print
    print "-"*17

  #------------------------
  # display current results on led
  #-----------------------
  def display(s):
    for x in xrange(8):
      for y in xrange(8):
        led8x8.setPixel(x, y, s.vars[y][x].get())

  #-----------------------
  # binarify
  #-----------------------
  def binarify(s,val):
    b = [0,]*8
    d = 0
    while val:
      b[d] = val&1
      val >>= 1
      d += 1
    return b

  #-----------------------
  # digify
  #-----------------------
  def digify(s,b):
    n = 0
    val = 0
    for d in b:
      val += d*(2**n)
      n += 1
    return val

  #-----------------------
  # clear it all
  #-----------------------
  def clear_all(s):
    print "clear all"
    for x in xrange(8):
      for y in xrange(8):
        s.vars[x][y].set(0)
    s.display()

  #-----------------------
  # save bitmap
  #-----------------------
  def save_bitmap(s):
    with open("bitmap.out","w") as FILE:
      FILE.write("{0}\n".format(led8x8.disp.getBuffer()))
          
  #-----------------------
  # save movie
  #-----------------------
  def save_movie(s):
    pickle.dump(s.movie,open('movie.mv','w'))
          
  #------------------------
  # save current frame
  #-----------------------
  def save_current_frame_new(s):
    s.movie[s.currentFrame][0]=copy.copy(led8x8.disp.getBuffer())
    print "currentFrame = {0}  movie = \n{1}".format(s.currentFrame,s.movie) 
    
  #------------------------
  # save current frame
  #-----------------------
  def save_current_frame(s):
    bitmap = []
    for row in xrange(8):
      vals = []
      for col in xrange(8):
        vals.append(s.vars[row][col].get())
      bitmap.append(s.digify(vals))
    s.movie[s.currentFrame] = [bitmap,s.DEFAULT_DT]
 
  #------------------------
  # load frame
  #-----------------------
  def load_frame_new(s, frameNumber):
    bitmap = s.movie[frameNumber][0]
    row = 0
    for rowVal in bitmap:
      #print rowVal
      checkVals = s.binarify(rowVal)
      #print checkVals
      checkVals = checkVals[7:] + checkVals[:7]
      #print checkVals
      col = 0
      for val in checkVals:
        s.vars[row][col].set(val)
        col += 1
      row += 1
    s.display()

  #------------------------
  # load frame
  #-----------------------
  def load_frame(s, frameNumber):
    bitmap = s.movie[frameNumber][0]
    row = 0
    for rowVal in bitmap:
      checkVals = s.binarify(rowVal)
      col = 0
      for val in checkVals:
        s.vars[row][col].set(val)
        col += 1
      row += 1
    s.display()

  #------------------------
  # add frame
  #-----------------------
  def add_frame(s):
    s.movie.append(copy.copy(s.DEFAULT_FRAME))

  #-----------------------
  # previous frame
  #-----------------------
  def prev_frame(s):
    #print len(s.movie), s.currentFrame
    if s.currentFrame==0:
       return
    s.save_current_frame()
    s.currentFrame -= 1
    s.load_frame(s.currentFrame)

  #-----------------------
  # next frame
  #-----------------------
  def next_frame(s):
    #print len(s.movie), s.currentFrame
    s.save_current_frame()
    if len(s.movie)==(s.currentFrame+1):
      s.clear_all()
      s.add_frame()
    s.currentFrame += 1
    s.load_frame(s.currentFrame)
    print s.movie
        
#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
root = Tk()
app = App(root)
root.mainloop()

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

import rectangle, random

class Cell(rectangle.Rectangle):
    def __init__(self, canvas, row, column):
        # make a 50x50 rectangle in the given row, column
        x0 = column * 12
        y0 = row * 12
        x1 = x0 + 12
        y1 = y0 + 12

        #generate a random rgb color
        self.rColor = lambda: random.randint(0,255)
        #the cells current state
        self.state = None
        #super to the Rectangle class
        super(Cell, self).__init__(canvas, (x0, y0, x1, y1), "gray")

    def set_state(self, state):
        #assign new state
        self.state = state

        #find the color for the cell
        color = "white" if state == True else "#1a1a1a"

        #configure the new color
        self.canvas.itemconfigure(self.canvas_id, fill=color, outline=color)


        #if self.state == True:
            #color = ('#%02X%02X%02X' % (self.rColor(),self.rColor(),self.rColor()))
            #self.canvas.itemconfigure(self.canvas_id, fill=color, outline=color)


    def toggle(self):
        #toggle the colors
        if self.state:
            self.set_state(False)
        else:
            self.set_state(True)

    def __copy__(self):
          return type(self)()

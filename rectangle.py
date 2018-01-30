try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class Rectangle(object):
    def __init__(self, canvas, coords, fill, outline=None):
        self.canvas = canvas
        self.outline = outline if outline is not None else fill
        self.fill = fill
        self.canvas_id = self.canvas.create_rectangle(
            coords, outline=self.outline, fill=self.fill)

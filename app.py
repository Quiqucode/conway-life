try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

import field, controls

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.field = field.Field(self)
        self.field.pack(side=tk.BOTTOM)

        self.controls = controls.Controls(self)
        self.controls.pack(side=tk.TOP, expand=True, fill=tk.X)

if __name__ == '__main__':
    app = Application()
    app.title("Conway's Game of Life")
    app.mainloop()

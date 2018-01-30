try:
    # for Python2
    import Tkinter as tk
    import ttk
except ImportError:
    # for Python3
    import tkinter as tk
    import tkinter.ttk as ttk

import copy

class Controls(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.master = master

        self.playToggle = False

        self.field = self.master.field

        self.generationCount = 0

        self.timeBetween = 50

        self.previous = []

        self.template = [[False for y in range(self.field.WIDTH)] for x in range(self.field.HEIGHT)]

        self.geneC = tk.Label(self, text="generation: " + str(self.generationCount))
        self.geneC.pack(side=tk.TOP, expand=True, fill=tk.X)

        self.stepB10 = ttk.Button(self, command=self.tickBackwardTen, text="<<<")
        self.stepB10.pack(side=tk.LEFT)
        self.stepB10.state(["disabled"])

        self.stepB = ttk.Button(self, command=self.tickBackward, text="<")
        self.stepB.pack(side=tk.LEFT)
        self.stepB.state(["disabled"])

        self.stepF10 = ttk.Button(self, command=self.tickForwardTen, text=">>>")
        self.stepF10.pack(side=tk.RIGHT)

        self.stepF = ttk.Button(self, command=self.tickForward, text=">")
        self.stepF.pack(side=tk.RIGHT)

        self.tPlay = ttk.Button(self, command=self.togglePlay, text="Play")
        self.tPlay.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        self.play()

    def tickForward(self, *args):
        self.generationCount += 1

        self.geneC['text'] = "generation: " + str(self.generationCount)

        self.previous.append(copy.deepcopy(self.template))

        for i in range(len(self.field.cells)):
            for j in range(len(self.field.cells[0])):
                self.previous[-1][i][j] = self.field.cells[i][j].state

        self.field.tick()

        self.stepB.state(["!disabled"])
        if self.generationCount >= 10:
            self.stepB10.state(["!disabled"])

    def tickBackward(self, *args):
        for i in range(len(self.field.cells)):
            for j in range(len(self.field.cells[0])):
                self.field.cells[i][j].set_state(self.previous[-1][i][j])

        self.previous = self.previous[:-1]

        if len(self.previous) < 1:
            self.stepB.state(["disabled"])
            self.stepB10.state(["disabled"])
        elif len(self.previous) > 1:
            self.stepB.state(["!disabled"])
            self.stepB10.state(["!disabled"])

        if len(self.previous) < 10:
            self.stepB10.state(["disabled"])
        elif len(self.previous) >= 10:
            self.stepB10.state(["!disabled"])
        self.generationCount = self.generationCount - 1

        self.geneC['text'] = "generation: " + str(self.generationCount)


    def togglePlay(self, *args):
        if self.tPlay["text"] == "Play":
            self.tPlay.configure(text="Pause")
            self.playToggle = True
        else:
            self.tPlay.configure(text="Play")
            self.playToggle = False

    def play(self):
        if self.playToggle:
            self.tickForward()

        self.after(self.timeBetween, self.play)

    def tickForwardTen(self):
        for _ in range(10):
            self.tickForward()

    def tickBackwardTen(self):
        for _ in range(10):
            self.tickBackward()

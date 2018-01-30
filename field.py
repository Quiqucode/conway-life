try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

import cell

class Field(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master)

        self.master = master

        self.HEIGHT = 36
        self.WIDTH = 40

        self.configure(height=self.HEIGHT*12, width=self.WIDTH*12)

        self.cells = [[cell.Cell(self, x, y) for y in range(self.WIDTH)] for x in range(self.HEIGHT)]

        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.cells[i][j].set_state(0)

        self.bind("<Button-1>", self.toggle)

        self.lastStep = self.cells

    def read(self):
        return [[True if self.cells[x][y].state == True else False for y in range(self.WIDTH)] for x in range(self.HEIGHT)]

    def returnCoords(self, event):
        return (event.x, event.y)

    def toggle(self, event):
        self.cells[int(self.returnCoords(event)[1]/12)][int(self.returnCoords(event)[0]/12)].toggle()

    def neighbors(self, row, col):
        count = 0

        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if not hor == ver == 0 and ((0 <= row + hor < self.WIDTH and 0 <= col + ver < self.HEIGHT)):
                    count += 1 if self.cells[(col + ver) % self.HEIGHT][(row + hor) % self.WIDTH].state else 0

        return count

    def tick(self):
        self.cellsToChange = []

        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j].state and self.neighbors(j, i) < 2:
                    self.cellsToChange.append([i, j])
                elif self.cells[i][j].state and self.neighbors(j, i) > 3:
                    self.cellsToChange.append([i, j])
                elif not self.cells[i][j].state and self.neighbors(j, i) == 3:
                    self.cellsToChange.append([i, j])

        for cell in self.cellsToChange:
            self.cells[cell[0]][cell[1]].toggle()

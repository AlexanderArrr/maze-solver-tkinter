import random
from time import sleep
from cell import Cell


class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()


    def _create_cells(self):
        for i in range(0, self.num_cols):
            col_cells = []
            for j in range(0, self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (self.cell_size_x * i)
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + (self.cell_size_y * j)
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols -1, self.num_rows - 1)


    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.02)
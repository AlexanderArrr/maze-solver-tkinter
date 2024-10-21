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
                 win=None,
                 ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = random.seed(random.random())

        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(0, self.num_cols):
            col_cells = []
            for j in range(0, self.num_rows):
                col_cells.append(Cell(self.win, i, j))
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
        rnd_i1 = random.randrange(0, self.num_cols - 1)
        rnd_j1 = random.choice((0, self.num_rows - 1))
        rnd_j2 = random.randrange(0, self.num_rows - 1)
        rnd_i2 = random.choice((0, self.num_cols - 1))
        
        if rnd_j1 == 0:
            self._cells[rnd_i1][0].has_top_wall = False
            self._draw_cell(rnd_i1, 0)
        else:
            self._cells[rnd_i1][rnd_j1].has_bottom_wall = False
            self._draw_cell(rnd_i1, rnd_j1) 
        if rnd_i2 == 0:
            self._cells[rnd_i2][0].has_left_wall = False
            self._draw_cell(rnd_i2, 0)
        else:
            self._cells[rnd_i2][rnd_j2].has_right_wall = False
            self._draw_cell(rnd_i2, rnd_j2)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        next_i = None
        next_j = None
        
        while True:
            to_visit = []
            
            # Check left
            if i > 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append(self._cells[i - 1][j])
            # Check right
            if i < (self.num_cols - 1):
                if not self._cells[i + 1][j].visited:
                    to_visit.append(self._cells[i + 1][j])
            # Check up
            if j > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append(self._cells[i][j - 1])
            # Check down
            if j < (self.num_rows - 1):
                if not self._cells[i][j + 1].visited:
                    to_visit.append(self._cells[i][j + 1])
            
            
            # No directions to go, break loop
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            # Randomly choose next direction
            direction = random.randrange(0, len(to_visit))
            current_cell = self._cells[i][j]
            next_cell = to_visit[direction]
            
            # Left direction
            if current_cell.x1 == next_cell.x2:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            # Right direction
            if current_cell.x2 == next_cell.x1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            # Up direction
            if current_cell.y1 == next_cell.y2:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            # Down direction
            if current_cell.y2 == next_cell.y1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            
            self._break_walls_r(next_cell.i, next_cell.j)


    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False            


    def _solve_r(self, i, j, exits, check=0):
        self.animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        # Check of return result (2 = Exits found, 1 = Need to backtrack, 0 = Continue)
        check = 0

        # Checking if exit cell was found
        if i == 0 and current_cell.has_left_wall == False:
            exits.append((i, j))
            if len(exits) == 1:
                current_cell.draw_circle(self.cell_size_x / 2)
        if i == self.num_cols - 1 and current_cell.has_right_wall == False:
            exits.append((i, j))
            if len(exits) == 1:
                current_cell.draw_circle(self.cell_size_x / 2)
        if j == 0 and current_cell.has_top_wall == False:
            exits.append((i, j))
            if len(exits) == 1:
                current_cell.draw_circle(self.cell_size_x / 2)
        if j == self.num_rows - 1 and current_cell.has_bottom_wall == False:
            exits.append((i, j))
            if len(exits) == 1:
                current_cell.draw_circle(self.cell_size_x / 2)
        if len(exits) == 2:
            current_cell.draw_circle(self.cell_size_x / 2)
            self.animate()
            return exits, 2
        
        # Checking and going in each direction
        if (i - 1) >= 0 and self._cells[i - 1][j].visited == False and self._cells[i - 1][j].has_right_wall == False:
            current_cell.draw_move(self._cells[i - 1][j])
            exits, new_check = self._solve_r(i - 1, j, exits)
            if new_check == 2:
                return exits, 2
            elif new_check == 1:
                current_cell.draw_move(self._cells[i - 1][j], undo=True)
        if (i + 1) < self.num_cols and self._cells[i + 1][j].visited == False and self._cells[i + 1][j].has_left_wall == False:
            current_cell.draw_move(self._cells[i + 1][j])
            exits, new_check = self._solve_r(i + 1, j, exits)
            if new_check == 2:
                return exits, 2
            elif new_check == 1:
                current_cell.draw_move(self._cells[i + 1][j], undo=True)
        if (j - 1) >= 0 and self._cells[i][j - 1].visited == False and self._cells[i][j - 1].has_bottom_wall == False:
            current_cell.draw_move(self._cells[i][j - 1])
            exits, new_check = self._solve_r(i, j - 1, exits)
            if new_check == 2:
                return exits, 2
            elif new_check == 1:
                current_cell.draw_move(self._cells[i][j - 1], undo=True)
        if (j + 1) < self.num_rows and self._cells[i][j + 1].visited == False and self._cells[i][j + 1].has_top_wall == False:
            current_cell.draw_move(self._cells[i][j + 1])
            exits, new_check = self._solve_r(i, j + 1, exits)
            if new_check == 2:
                return exits, 2
            elif new_check == 1:
                current_cell.draw_move(self._cells[i][j + 1], undo=True)

        return exits, 1


    def solve(self):
        exits = []
        check = 0
        exits, check = self._solve_r(0, 0, exits, check)
        if len(exits) == 2 and check == 2:
            print(f"Two exits found at i{exits[0][0]} & j{exits[0][1]} and i{exits[1][0]} & j{exits[1][1]}!")
        else:
            print("No exits found!")


    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.02)



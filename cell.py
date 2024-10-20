from graphics import Line, Point

class Cell:
    def __init__(self, win, i=None, j=None):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win
        
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

        self.visited = False
        self.i = i
        self.j = j

    def draw(self, x1, y1, x2, y2):
        if self.win == None:
            return
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        bgcolor = self.win.root.cget('bg')
        
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")
        else:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), bgcolor)
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
        else:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), bgcolor)
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
        else:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), bgcolor)
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")
        else:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), bgcolor)

    def draw_move(self, to_cell, undo=False):
        line_color = "black"
        if undo:
            line_color = "red"
        from_center_x = self.x1 + abs(((self.x2 - self.x1) // 2))
        from_center_y = self.y1 + abs(((self.y2 - self.y1) // 2))
        to_center_x = to_cell.x1 + abs(((to_cell.x2 - to_cell.x1) // 2))
        to_center_y = to_cell.y1 + abs(((to_cell.y2 - to_cell.y1) // 2))
        self.win.draw_line(Line(Point(from_center_x, from_center_y), Point(to_center_x, to_center_y)), line_color)

    def draw_circle(self, r):
        from_center_x = self.x1 + abs(((self.x2 - self.x1) // 2))
        from_center_y = self.y1 + abs(((self.y2 - self.y1) // 2))
        x0 = from_center_x - r
        y0 = from_center_y - r
        x1 = from_center_x + r
        y1 = from_center_y + r
        self.win.canvas.create_oval(x0, y0, x1, y1)
        
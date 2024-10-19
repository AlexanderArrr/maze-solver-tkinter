from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win
        
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self.win == None:
            return
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        from_center_x = self.x1 + abs(((self.x2 - self.x1) // 2))
        from_center_y = self.y1 + abs(((self.y2 - self.y1) // 2))
        to_center_x = to_cell.x1 + abs(((to_cell.x2 - to_cell.x1) // 2))
        to_center_y = to_cell.y1 + abs(((to_cell.y2 - to_cell.y1) // 2))
        self.win.draw_line(Line(Point(from_center_x, from_center_y), Point(to_center_x, to_center_y)), line_color)
        
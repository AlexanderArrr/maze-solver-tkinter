from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    # line = Line(Point(400, 400), Point(600,450))
    # win.draw_line(line, "black")
    cell = Cell(2, 2, 200, 200, win)
    # cell.has_left_wall = False
    # cell.has_top_wall = False
    cell.draw()

    win.wait_for_close()

main()
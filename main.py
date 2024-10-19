from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    # line = Line(Point(400, 400), Point(600,450))
    # win.draw_line(line, "black")
    cell = Cell(win)
    cell.has_right_wall = False
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell.draw(0, 0, 200, 200,)
    cell2.draw(200, 0, 400, 200)
    cell.draw_move(cell2)

    win.wait_for_close()

main()
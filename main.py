from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell2.has_bottom_wall= False
    cell3 = Cell(win)
    cell3.has_bottom_wall=False
    cell3.has_right_wall=False
    cell4 = Cell(win)
    cell4.has_top_wall=False
    cell4.has_left_wall=False
    cell5 = Cell(win)
    cell1.draw(0, 0, 50, 50)       # Top-left cell
    cell2.draw(50, 0, 100, 50)     # Top-right cell
    cell3.draw(0, 50, 50, 100)     # Bottom-left cell
    cell4.draw(50, 50, 100, 100)   # Bottom-right cell
    cell5.draw(400, 400, 450, 450) # Separate cell
    cell2.draw_move(cell4)
    cell4.draw_move(cell3, undo=True)    
    win.draw_line(Line(Point(0, 300), Point(400, 300)), "#F4F4F4")
    win.wait_for_close()

main()
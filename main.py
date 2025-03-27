from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(400, 300)), "#F4F4F4")
    win.wait_for_close()

main()
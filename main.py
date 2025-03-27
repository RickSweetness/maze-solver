from graphics import Window, Line, Point, Cell
from maze import Maze






def main():
    win = Window(800, 600)
    maze = Maze(
        25,
        25,
        15,
        11,
        50,
        50,
        win
    )
    win.wait_for_close()

main()
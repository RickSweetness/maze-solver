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
        win,
        seed=None
    )
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

main()
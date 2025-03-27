from graphics import Cell, Line, Point
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            cell_row = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                cell_row.append(cell)
            self._cells.append(cell_row)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cells(i, j)

    def draw_cells(self, i, j):
        if self.win is None:
            return
        x1 = (j * self.cell_size_x) + self.x1
        y1 = (i * self.cell_size_y) + self.y1
        x2 = ((j + 1) * self.cell_size_x) + self.x1
        y2 = ((i + 1) * self.cell_size_y) + self.y1
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
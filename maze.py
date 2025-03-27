from graphics import Cell, Line, Point
import time, random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        random.seed(seed)
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
        time.sleep(0.015)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self.draw_cells(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self.draw_cells(self.num_cols-1, self.num_rows-1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i-1 >= 0:
                if self._cells[i-1][j].visited == False:
                    possible_directions.append(self._cells[i-1][j])
            if i+1 < len(self._cells):
                if self._cells[i+1][j].visited == False:
                    possible_directions.append(self._cells[i+1][j])
            if j-1 >= 0:
                if self._cells[i][j-1].visited == False:
                    possible_directions.append(self._cells[i][j-1])
            if j+1 < len(self._cells[0]):
                if self._cells[i][j+1].visited == False:
                    possible_directions.append(self._cells[i][j+1])
            if len(possible_directions) == 0:
                self.draw_cells(i, j)
                return
            else:
                direction = possible_directions.pop(random.randrange(len(possible_directions)))
            if i-1 >= 0 and direction == self._cells[i-1][j]:
                self._cells[i][j].has_top_wall = False
                self.draw_cells(i, j)
                direction.has_bottom_wall = False
                self.draw_cells(i-1, j)
                self._break_walls_r(i-1, j)
            elif i+1 < len(self._cells) and direction == self._cells[i+1][j]:
                self._cells[i][j].has_bottom_wall = False
                self.draw_cells(i, j)
                direction.has_top_wall = False
                self.draw_cells(i+1, j)
                self._break_walls_r(i+1, j)
            elif j-1 >= 0 and direction == self._cells[i][j-1]:
                self._cells[i][j].has_left_wall = False
                self.draw_cells(i, j)
                direction.has_right_wall = False
                self.draw_cells(i, j-1)
                self._break_walls_r(i, j-1)
            elif j+1 < len(self._cells[0]) and direction == self._cells[i][j+1]:
                self._cells[i][j].has_right_wall = False
                self.draw_cells(i, j)
                direction.has_left_wall = False
                self.draw_cells(i, j+1)
                self._break_walls_r(i, j+1)
    
    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
    
    def solve(self):
        if self._solve_r(0, 0):
            return True
        else:
            return False
        
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[len(self._cells)-1][len(self._cells[0])-1]:
            return True
        possible_directions = []
        if i-1 >= 0:
            if self._cells[i-1][j].visited == False and self._cells[i-1][j].has_bottom_wall == False:
                current_cell.draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                else:
                    current_cell.draw_move(self._cells[i-1][j], undo=True)
        if i+1 < len(self._cells):
            if self._cells[i+1][j].visited == False and self._cells[i+1][j].has_top_wall == False:
                current_cell.draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                else:
                    current_cell.draw_move(self._cells[i+1][j], undo=True)
        if j-1 >= 0:
            if self._cells[i][j-1].visited == False and self._cells[i][j-1].has_right_wall == False:
                current_cell.draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                else:
                    current_cell.draw_move(self._cells[i][j-1], undo=True)
        if j+1 < len(self._cells[0]):
            if self._cells[i][j+1].visited == False and self._cells[i][j+1].has_left_wall == False:
                current_cell.draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                else:
                    current_cell.draw_move(self._cells[i][j+1], undo=True)
        

            


import unittest
from maze import Maze
from graphics import Window
import random

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_many_cell(self):
        num_cols = 100
        num_rows = 50
        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        self.assertEqual(len(m1._cells)*len(m1._cells[0]), 5000)
    
    def test_break_walls_start(self):
        m1 = Maze(0, 0, 10, 10, 50, 50)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_left_wall)
        self.assertFalse(m1._cells[9][9].has_right_wall)
    
    def test_reset_cells(self):
        m1 = Maze(0, 0, 10, 10, 50, 50)
        m1._break_walls_r(0, 0)
        for i in range(10):
            for j in range(10):
                self.assertTrue(m1._cells[i][j].visited)        
        m1._reset_cells_visited()
        for i in range(10):
            for j in range(10):
                self.assertFalse(m1._cells[i][j].visited)

    

if __name__ == "__main__":
    unittest.main()
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("A-Maze-ing")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="#36454F")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running == True:
            self.redraw()
    
    def close(self):
        self.__is_running = False
    
    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, canvas, fill_colour):
        canvas.create_line(
    self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_colour, width=2
)

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "#F4F4F4")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "#F4F4F4")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "#F4F4F4")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "#F4F4F4")
        if self.has_left_wall ==  False:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "#36454F")
        if self.has_top_wall == False:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "#36454F")
        if self.has_right_wall == False:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "#36454F")
        if self.has_bottom_wall == False:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "#36454F")

        
    def draw_move(self, to_cell, undo=False):
        self_midpoint = Point((self._x1 + self._x2)//2, (self._y1 + self._y2)//2)
        to_cell_midpoint = Point(((to_cell._x1 + to_cell._x2)//2), ((to_cell._y1 + to_cell._y2)//2))
        if undo == False:
            fill_colour = "#D32F2F"
        else:
            fill_colour = "#B0B0B0"
        self._win.draw_line(Line(self_midpoint, to_cell_midpoint), fill_colour)

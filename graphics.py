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
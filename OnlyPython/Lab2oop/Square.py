from Lab2oop import Rectangle
from Lab2oop import Color
class Square(Rectangle.Rectangle):
    def __init__(self, _len, _color):
        self.name = "квадрат"
        self.len = _len
        self.color = _color
    def Area(self):
        return self.len*self.len
    def repr(self):
        f_str = "Это {0} {2} со значением яркости {3}, размером {1} и площадью {4}".format(self.color.color, self.len, self.name, self.color.brightness, self.Area())
        print(f_str)
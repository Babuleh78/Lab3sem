from Lab2oop import GeometricShape
from Lab2oop import Color
class Rectangle(GeometricShape.GeometricalShape):
    def __init__(self, _w, _h, _c):
        self.name = "прямоугольник"
        self.width = _w
        self.height = _h
        self.color = _c
    def Area(self):
        return self.width*self.height
    def repr(self):
        f_str = "Это {0} {3} со значением яркости {4}, размером {1} на {2} и площадью {5}".format(self.color.color, self.width, self.height, self.name,self.color.brightness, self.Area() )
        print(f_str)
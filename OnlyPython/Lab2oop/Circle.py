from Lab2oop import GeometricShape
from Lab2oop import Color
import math

class Circle(GeometricShape.GeometricalShape):
    def __init__(self, _r, _c):
        self.name = "круг"
        self.r = _r
        self.color = _c
    def Area(self):
        return math.pi*self.r*self.r
    def repr(self):
        f_str = "Это {0} {2} со значением яркости {3}, радиусом {1} и площадью {4}".format(self.color.color, self.r, self.name, self.color.brightness, self.Area())
        print(f_str)
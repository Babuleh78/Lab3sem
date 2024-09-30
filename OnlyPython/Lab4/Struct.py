from abc import ABC, abstractmethod
#Bridge
class Color(ABC): #Абстракция
    @abstractmethod
    def get_color(self):
        pass

class Red(Color): #Реализация
    def get_color(self):
        return "красный"
    
class Blue(Color): #Реализация
    def get_color(self):
        return "синий"
    
class Shape(ABC): #Абстракция с ссылкой на реализацию
    def __init__(self, color: Color):
        self.color = color
    @abstractmethod
    def info(self):
        pass

class Square(Shape):
    def info(self):
        return f"Квадрат, цвет: {self.color.get_color()}"
    
class Circle(Shape):
    def info(self):
        return f"Окружность, цвет: {self.color.get_color()}"
    

red = Red()
blue = Blue()
square_red = Square(red)
circle_blue = Circle(blue)
print(square_red.info())
print(circle_blue.info())  
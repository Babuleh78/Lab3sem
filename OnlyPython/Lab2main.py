from Lab2oop.Circle import Circle
from Lab2oop.Rectangle import Rectangle
from Lab2oop.Square import Square
from Lab2oop.Color import Color
import numpy as np
def main():
    blue = Color()
    blue.setcolor("синий")
    green = Color()
    green.setcolor("зеленый")
    red = Color()
    red.setcolor("красный")
    rect = Rectangle(14, 14, blue)
    circ = Circle(4, green)
    sq = Square(14, red)
    Shapes = np.array([circ, rect, sq])
    for shape in Shapes:
        shape.repr()
if __name__ == "__main__":
    main()
class Color:
    def __init__(self):
        self.brightness = 1.0
        self.color = "черный"
    def getcolor(self):
        return self.color
    def getbrightness(self):
        return self.brightness
    def setcolor(self, s):
        self.color = s
    def setbrightness(self, a):
        self.brightness = a
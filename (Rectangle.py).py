import math

class Rectangle:

    def __init__(self, width = 1.0, height = 2.0):
        self.width = width
        self.height = height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def __str__(self):
        return f"Width: {str(self.width)} | Height: {str(self.height)} | Area: {str(self.getArea())} | Perimeter: {str(self.getPerimeter())}"

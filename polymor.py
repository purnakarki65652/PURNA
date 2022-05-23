from math import pi
class square:
    def __init__(self, length):
        self.l = length
    def perimeter(self):
        return 4 * (self.l)
    def area(self):
        return  self.l * self.l
class Circle:
    def __init__(self, radius):
        self.r = radius
    def perimeter(self):
        return 2 * pi * self.r
    def area(self):
        return pi * self.r ** 2
    # initialize the classes
sqr = square(10)
c1 = Circle(4)
print("perimeter computed for square: ", sqr.perimeter())
print("Area computed for square: ", sqr.area())
print("perimeter computed for circle: ", c1.perimeter())
print("Area computed for circle: ", c1.area())
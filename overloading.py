class Baseclass:
    def __init__(self, name):
        self.name = name
    def area1(self):
        pass
    def __str__(self):
        return self.name
class Rectangle(Baseclass):
    def __init__(self, length, breadth):
        super().__init__("rectangle")
        self.length = length
        self.breadth = breadth
    def area1(self):
        return self.length * self.breadth
class Triangle(Baseclass):
    def __init__(self, heigth, base):
        super().__init__("triangle")
        self.height = heigth
        self.base = base
    def area1(self):
        return (self.base * self.height) / 2
a = Rectangle(90, 80)
b = Triangle(77, 64)
print("The shape is :", b)
print("The area of shape is", b.area1())
print("The shape is:", a)
print("The area of shape is", a.area1())

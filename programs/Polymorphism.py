#            ​ Polymorphism example:
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area = 3.14*self.radius**2
        print("Area of circle is: ",area)

class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def calculate_area(self):
        area = self.l * self.b
        print("Area of rectangle is: ",area)

class Square:
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        area = self.side*self.side
        print("Area of square is: ",area)

def print_area(shape):
    shape.calculate_area()


c = Circle(5)
r = Rectangle(4,9)
s = Square(8)
print_area(c)
print_area(r)
print_area(s)

'''
Output:
Area of circle is:  78.5
Area of rectangle is:  36
Area of square is:  64
'''

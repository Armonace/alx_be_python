import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method.")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Demonstration of polymorphism
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3)
    ]

    for shape in shapes:
        print(f"{type(shape).__name__} Area: {shape.area():.2f}")

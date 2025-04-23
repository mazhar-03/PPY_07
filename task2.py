import math
from math import pi, sqrt
from functools import singledispatch

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

@singledispatch
def area(shape, *args, **kwargs):
    raise NotImplementedError("Cannot compute area for this shape.")

@singledispatch
def perimeter(shape, *args, **kwargs):
    raise NotImplementedError("Cannot compute perimeter for this shape.")

@area.register(Circle)
def _(shape, *args, **kwargs):
    return pi * shape.radius ** 2

@perimeter.register(Circle)
def _(shape, *args, **kwargs):
    return 2 * pi * shape.radius

@area.register(Rectangle)
def _(shape, *args, **kwargs):
    return shape.width * shape.height

@perimeter.register(Rectangle)
def _(shape, *args, **kwargs):
    return 2 * (shape.width + shape.height)

@perimeter.register(Triangle)
def _(shape, *args, **kwargs):
    return shape.a + shape.b + shape.c

@area.register(Triangle)
def _(shape, *args, **kwargs):
    p = perimeter(shape, *args, **kwargs) / 2
    return math.sqrt(p * (p-shape.a) * (p - shape.b) * (p- shape.c))


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
    Circle(2.5),
    Rectangle(10, 3)
]

for shape in shapes:
    print(f"Shape: {shape.__class__.__name__}")
    print(f"Area: {area(shape):.2f}")
    print(f"Perimeter: {perimeter(shape):.2f}")
    print("-" * 20)
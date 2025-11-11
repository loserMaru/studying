import abc


class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def area(self): pass

    def print_point(self):
        print("X: ", self.x, "\tY: ", self.y)


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self): return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): return self.radius * self.radius

def print_area(shape):
    print("Area is", shape.area())


# print_area(Rectangle(100, 200))
print_area(Circle(50))

rect = Rectangle(5, 10, 100, 100)
rect.print_point()
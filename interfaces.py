from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(f'Площадь: {shape.area()} \tПериметр: {shape.perimeter()}')
print()


class FileWriter:
    def write(self, text):
        print('Записываю данные в файл: ', text)


class NetworkWriter:
    def write(self, text):
        print('Отправляю данные по сети: ', text)


def save_data(writer, data):
    writer.write(data)


save_data(FileWriter(), 'Hello World!')
save_data(NetworkWriter(), 'Hello World!')

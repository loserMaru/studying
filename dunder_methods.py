import math
from functools import total_ordering


@total_ordering
class Vector2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        # цель: отладочная строка, желательна возможность eval() в идеале
        return f"Vector2D({self.x!r}, {self.y!r})"

    def __str__(self):
        # человекочитаемая форма
        return f"({self.x:.3f}, {self.y:.3f})"

    def __eq__(self, other):
        # сравниваем по компонентам; если другой тип — вернуть NotImplemented
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        # определим порядок по длине вектора (норма)
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.length() < other.length()

    def __add__(self, other):
        # сложение векторов
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def length(self):
        return math.hypot(self.x, self.y)


# Демонстрация:
a = Vector2D(1, 2)
b = Vector2D(3, 4)
print("repr:", repr(a))  # repr: Vector2D(1.0, 2.0)
print("str:", str(a))  # str: (1.000, 2.000)
print("add:", a + b)  # add: (4.000, 6.000)
print("eq:", a == Vector2D(1, 2))  # True
print("lt:", a < b)  # True (по длине)

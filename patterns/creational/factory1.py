"""Демонстратор фабричного метода."""

from enum import Enum
from math import cos, sin, pi


class CoordinateSystem(Enum):
    CARTESIAN = 0
    POLAR = 1


class Point:
    """Описывает точку на плоскости."""

    # неэффективный конструктор: нарушение OCP, неочевидные имена параметров, сложная документация
    # def __init__(self,
    #              a: float,
    #              b: float,
    #              coords: CoordinateSystem = CoordinateSystem.CARTESIAN):
    #     if coords is CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif coords is CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # фабричный метод
    @classmethod
    def cartesian(cls, x: float, y: float) -> 'Point':
        """"""
        return cls(x, y)

    # фабричный метод
    @classmethod
    def polar(cls, rho: float, phi: float) -> 'Point':
        """"""
        x = rho * cos(phi)
        y = rho * sin(phi)
        return cls(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"


zero = Point(0, 0)
p1 = Point.cartesian(2, 3.5)
p2 = Point.polar(1.5, pi/6)
print(zero, p1, p2, sep='\n')

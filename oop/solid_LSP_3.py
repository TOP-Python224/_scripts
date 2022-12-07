"""Liskov Substitution Principle — Принцип Подстановки Лисков"""

from numbers import Number
from decimal import Decimal as dec


class Rectangle:
    def __init__(self, width: str | Number, height: str | Number):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self._width = dec(str(value))
        elif isinstance(value, dec):
            self._width = value
        else:
            self._width = dec(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)):
            self._height = dec(str(value))
        elif isinstance(value, dec):
            self._height = value
        else:
            self._height = dec(value)

    @property
    def area(self):
        return self._width*self._height


class Square(Rectangle):
    def __init__(self, side: str | Number):
        super().__init__(side, side)

    # переопределения сеттеров нарушают LSP
    @Rectangle.width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self._width = dec(str(value))
            self._height = dec(str(value))
        elif isinstance(value, dec):
            self._width = value
            self._height = value
        else:
            self._width = dec(value)
            self._height = dec(value)

    @Rectangle.height.setter
    def height(self, value):
        if isinstance(value, (int, float)):
            self._width = dec(str(value))
            self._height = dec(str(value))
        elif isinstance(value, dec):
            self._width = value
            self._height = value
        else:
            self._width = dec(value)
            self._height = dec(value)



def high_lvl_func(rc: Rectangle):
    width = rc.width
    rc.height = 10
    print(f'Expected area: {width*10}')
    print(f'Calculated area: {rc.area}')



rc1 = Rectangle('7.5', 1.2)
print(rc1.__dict__)

sq1 = Square(5)
print(sq1.__dict__)

sq1.height = 8
print(sq1.__dict__)

print('\nrc1')
high_lvl_func(rc1)

print('\nsq1')
high_lvl_func(sq1)

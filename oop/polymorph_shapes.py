from dataclasses import dataclass
from math import pi


@dataclass
class Circle:
    radius: float

    @property
    def area(self) -> float:
        return 2*pi*self.radius


@dataclass
class Square:
    side: float

    @property
    def area(self) -> float:
        return self.side**2


@dataclass
class Triangle:
    base: float
    height: float

    @property
    def area(self) -> float:
        return 0.5*self.base*self.height


shapes = [
    Circle(5),
    Triangle(4, 3),
    Square(4.4)
]

for shape in shapes:
    print(shape.__class__.__name__, shape.area)


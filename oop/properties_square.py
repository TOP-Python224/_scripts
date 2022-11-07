class Square:
    def __init__(self, side: float):
        self._side = side
        self._perimeter = 4*side
        self._area = side**2

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, new_side: float):
        self._side = new_side
        self._perimeter = 4*new_side
        self._area = new_side**2

    @property
    def perimeter(self) -> float:
        return self._perimeter

    @perimeter.setter
    def perimeter(self, new_perimeter: float):
        self._side = new_perimeter / 4
        self._perimeter = new_perimeter
        self._area = self._side**2

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, new_area: float):
        self._side = new_area**0.5
        self._perimeter = 4*self._side
        self._area = new_area

    def __repr__(self):
        return f'<Square:' \
               f' side={self._side:.2f},' \
               f' per={self._perimeter:.2f},' \
               f' area={self._area:.2f}>'


sq1 = Square(5)
print(sq1)

sq1.area = 36
print(sq1)

sq1.perimeter = 50
print(sq1)

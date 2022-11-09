from numbers import Real


Coordinates = tuple[Real, Real]

class Point:
    """Описывает точку на плоскости в декартовой системе координат."""
    def __init__(self, x: Real, y: Real):
        self.x = x
        self.y = y

    # p1 < axes_zero
    # p1.__lt__(axes_zero)
    def __lt__(point1, point2) -> bool:
        if isinstance(point2, Point):
            return point1.x < point2.x and point1.y < point2.y
        elif isinstance(point2, tuple):
            if len(point2) == 2:
                x, y = point2
                if isinstance(x, Real) and isinstance(y, Real):
                    return point1.x < x and point1.y < y
        else:
            raise TypeError

    # p1 - axes_zero
    # p1.__sub__(axes_zero)
    def __sub__(point, other):
        """Вычисляет и возвращает расстояние между двумя точками."""
        if isinstance(other, Point):
            return ((point.x - other.x)**2 + (point.y - other.y)**2)**0.5
        elif isinstance(other, Real):
            return point - Point(other, other)
        else:
            raise TypeError

    # 5 - p2
    # p2.__rsub__(5)
    def __rsub__(point, other):
        if isinstance(other, Real):
            return point - Point(other, other)
        else:
            raise TypeError


axes_zero = Point(0, 0)

p1 = Point(1, 1)
p2 = Point(-2, -3)

print(p1 < axes_zero)
print(p1 < (5, 5))
print(p2 < axes_zero)

print(p1 - axes_zero)
print(p1 - 12)
print(5 - p2)

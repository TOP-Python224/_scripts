from random import randint as ri

p1 = (1, 3)

def point_x(point: tuple[int, int]) -> int:
    return point[1]

res1 = point_x(p1)
print(f'{point_x = }')
print(f'{point_x.__name__ = }')
print(f'{res1 = }\n')


lf = lambda point: point[ri(0, 1)]

res2 = lf(p1)
print(f'{lf = }')
print(f'{lf.__name__ = }')
print(f'{res2 = }\n')


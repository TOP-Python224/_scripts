from collections import namedtuple as nt, ChainMap as CM

Person = nt('Person', ['name', 'age'])
pers1 = Person('Георгий', 38)
print(pers1)


PointsTable = nt('PointsTable', ['x', 'y'])
experimental_data = PointsTable(
    x=(0.1, 0.23, -0.19, 0.02, 0.3),
    y=(5, 4.5, 1.5, 3, 8)
)
print(sum(experimental_data.x), end='\n\n')



d1 = {'z': 1, 'a': 59, 'm': 19}
d2 = {'x': 4, 'a': -20, 'n': 25}
cm1 = CM(d1, d2)

for elem in cm1.items():
    print(elem)
print()

for elem in (d1 | d2).items():
    print(elem)
print()

d1 |= {'o': 21}
print(cm1)

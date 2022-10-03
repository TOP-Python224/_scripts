from itertools import accumulate, chain, dropwhile, takewhile, pairwise, starmap, zip_longest

for n in accumulate(range(10)):
    print(n, end=' ')
print('\n')

for n in accumulate(range(1, 10), lambda n, m: n - m):
    print(n, end=' ')
print('\n')


r1 = range(10, 100, 10)
d1 = {'a': 1, 'b': 2}

for elem in chain(r1, d1.items()):
    print(elem, end=' ')
print('\n')


def predicate1(x: int):
    return x < 5

for n in dropwhile(predicate1, [1, 4, 6, 4, 1]):
    print(n, end=' ')
print('\n')

for n in takewhile(predicate1, [1, 4, 6, 4, 1]):
    print(n, end=' ')
print('\n')


for n in pairwise(range(1, 5)):
    print(n, end=' ')
print('\n')


for n in starmap(pow, [(2, 5), (3, 2), (10, 3)]):
    print(n, end=' ')
print('\n')


for pair in zip(range(5), range(7)):
    print(pair, end=' ')
print('\n')

for pair in zip_longest(range(5), range(7), fillvalue=0):
    print(pair, end=' ')
print('\n')

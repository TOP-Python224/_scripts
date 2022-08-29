from typing import Callable, Iterable
from random import randrange as rr


def mymap(function: Callable, iterator: Iterable):
    """Собственная реализация встроенной функции map."""
    ret = []
    for elem in iterator:
        ret += [function(elem)]
    return ret


def zbc(obj):
    return len(str(obj))

data_test = [rr(100,) for _ in range(10)]
ret_test = mymap(zbc, data_test)
map_test = map(zbc, data_test)

print(ret_test, end='\n\n')
print(map_test, end='\n\n')

print(list(map_test))

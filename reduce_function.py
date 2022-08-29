# [1, 2, 3, 4, 5]
# (((1 + 2) + 3) + 4) + 5

from typing import Callable, Iterable
from random import randrange as rr
from functools import reduce


def myreduce(function: Callable, iterator: Iterable):
    listed_iterator = list(iterator)
    if len(listed_iterator) < 2:
        raise ValueError('iterator should contain at least two elements')
    res = function(listed_iterator[0], listed_iterator[1])
    for i in range(2, len(listed_iterator)):
        res = function(res, listed_iterator[i])
    return res


def adder(num1, num2):
    return num1 + num2


data_test = [rr(10) for _ in range(10)]
print(f'{data_test = }')
print(f'({sum(data_test)})')

print(f'{myreduce(adder, data_test)}')
print(f'{reduce(adder, data_test)}')

myreduce(adder, [1])

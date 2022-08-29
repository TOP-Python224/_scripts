from typing import Callable

def test():
    """Демонстрационная функция."""
    print('вызов функции test()')

print(f'{test = }')
print(f'{type(test) = }')
print(f'{test.__name__ = }\n')

var = test

print(f'{var = }')
print(f'{type(var) = }')
print(f'{var.__name__ = }\n')

test()
var()
print()

def high(func_obj: Callable, *args, **kwargs):
    """Пример функции высшего порядка."""
    print('вызов функции высшего порядка high()')
    ret = func_obj(*args, **kwargs)
    print(f'{ret = }')

high(test)
print()

def adder(num1: int, num2: int) -> int:
    return num1 + num2

high(adder, 5, 6)
print()

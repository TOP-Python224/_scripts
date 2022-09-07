from typing import SupportsFloat, Callable
from functools import reduce


def adder(*args: SupportsFloat) -> float:
    return float(sum(args))

def multiplicator(*args: SupportsFloat) -> float:
    # reduce(lambda x, y: x*y, [1, 2, 3, 4]) -> ((1 * 2) * 3) * 4
    return reduce(lambda x, y: x*y, args)


def high(func_obj: Callable, *args: SupportsFloat):
    print('high: до вызова переданной функции')
    for num in args:
        if not isinstance(num, (int, float)):
            print(f'{func_obj.__name__} принимает только объекты чисел')
            return None
    res = func_obj(*args)
    print('high: после вызова переданной функции')
    return res



# print(f'{high(adder, 4, "abc", 12, -8) = }\n')
# print(f'{high(multiplicator, 4, 6, 12, -8) = }\n')



def decorator(func_obj: Callable) -> Callable:
    
    def _wrapper(*args):
        print(f'decorator: до вызова функции {func_obj.__name__}')
        print(f'\targs = {", ".join(str(arg) for arg in args)}')
        res = func_obj(*args)
        print(f'decorator: после вызова функции {func_obj.__name__}')
        print(f'\t{res = }')
        return res

    return _wrapper


test = decorator(adder)
print(f'{test = }\n{type(test) = }\n')

# test()
# print()
# test(1, 2, 3, 4, 5)
# print('\n')

print(f'{adder = }\n{type(adder) = }\n')
adder = decorator(adder)
print(f'{adder = }\n{type(adder) = }\n')

adder()
# print('\n')


@decorator
def subber(*args: SupportsFloat) -> float:
    return reduce(lambda x, y: x - y, args)
# subber = decorator(subber)

# subber(100, 20, 10, 5)
print(f'{subber = }\n{type(subber) = }\n')

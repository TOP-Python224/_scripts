from json import load as jload
from pathlib import Path
from sys import path

numbers_path = Path(path[0]) / 'numbers_en.json'


# mixin class
class NumberNames:
    with open(numbers_path, encoding='utf-8') as filein:
        _names = {int(k): v for k, v in jload(filein).items()}


class NamedInt(int, NumberNames):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        cls.__post_init__(instance)
        return instance

    def __post_init__(self):
        o = self % 10
        t = self % 100 - o
        h = self % 1000 - t - o
        name = self._names[h] + ' ' if h else ''
        if t == 10 and 1 <= o <= 9:
            name += self._names[t + o] + ' '
        else:
            name += (self._names[t] + ' ' if t else '') + self._names[o]
        self.name = name.strip()

    def __adder(self, other: int) -> 'NamedInt':
        if isinstance(other, int):
            return NamedInt(super().__add__(other))
        else:
            raise TypeError

    # n + 7:  n -> self,  7 -> other
    def __add__(self, other: int) -> 'NamedInt':
        return self.__adder(other)

    # 10 + n:  10 -> other,  n -> self
    def __radd__(self, other: int) -> 'NamedInt':
        return self.__adder(other)

    # n += 19:  n -> self,  19 -> other
    def __iadd__(self, other: int) -> 'NamedInt':
        return self.__adder(other)

    def __str__(self):
        return self.name


# for n in range(1, 1000):
#     print(NamedInt(n))

n = NamedInt(5)

r = n + 7
print(r)

r = 10 + n
print(r)

n += 19
print(n)

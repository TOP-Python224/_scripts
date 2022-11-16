class NamedInt(int):
    __names = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот', 0: ''
    }

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        cls.__post_init__(instance)
        return instance

    def __post_init__(self):
        o = self % 10
        t = self % 100 - o
        h = self % 1000 - t - o
        name = self.__names[h] + ' ' if h else ''
        if t == 10 and 1 <= o <= 9:
            name += self.__names[t+o] + ' '
        else:
            name += (self.__names[t] + ' ' if t else '') + self.__names[o]
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

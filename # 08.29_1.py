from math import log10, ceil
from typing import Iterable, Callable
from numbers import Real


nominals = {
    "E6": (10, 15, 22, 33, 47, 68),
    "E12": (10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82),
    "E24": (10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91),
    "E48": (100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953),
    "E96": (100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976)
}

def exp_base10(number: Real, exp: int = 1) -> Real:
    """Возвращает число, умноженное на 10 в степени exp."""
    return number * 10**exp


def abs_sub(number1: Real, number2: Real) -> Real:
    return abs(number1 - number2)


def map_two_arg(func_object: Callable, iterator: Iterable, arg2=None) -> tuple:
    """Возвращает кортеж с возвращаемыми значениями функции func_object(), вызванной с одним или двумя аргументами: элементом последовательности и значением параметра функции func_object() по умолчанию, либо arg2."""
    res = ()
    for elem in iterator:
        if arg2 is None:
            res += (func_object(elem), )
        else:
            res += (func_object(elem, arg2), )
    return res


def choose_nominal(required_nominal: Real) -> dict[str, int]:
    """Возвращает ближайший к переданному номинал сопротивления из каждого ряда сопротивлений."""
    res = dict.fromkeys(nominals)
    for key, row in nominals.items():
        if not (min(row) <= required_nominal <= max(row)):
            # на сколько порядков отличается переданный номинал от базовых номиналов ряда
            exp = ceil(log10(required_nominal // max(row)))
            # приведение базовых номиналов ряда к одному порядку с переданным номиналом
            row = map_two_arg(exp_base10, row, exp)
        # вычисление модулей разности каждого числа ряда с переданным номиналом
        row_delta = map_two_arg(abs_sub, row, required_nominal)
        # поиск индекса минимальной разности
        i = row_delta.index(min(row_delta))
        res[key] = row[i]
    return res


nominal = int(input(' величина сопротивления в Ом > '))
resistors = choose_nominal(nominal)
print(resistors)


# expected:
#  величина сопротивления в Ом > 500
# resistors -> {'E6': 470, 'E12': 470, 'E24': 510, 'E48': 511, 'E96': 499}

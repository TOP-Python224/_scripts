from collections.abc import Callable
from numbers import Real

import operator as op


class Calculator:
    def __init__(self, number1: Real, number2: Real):
        self.number1 = number1
        self.number2 = number2

    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.number1 == other.number1 and self.number2 == other.number2
        else:
            raise TypeError

    def calculate(self, operation: Callable[[Real, Real], Real]) -> Real:
        """Метод-интерфейс для различных стратегий поведения — математических операций, выполняемых с числами number1 и number2.

        :param operation: вызываемый объект, принимающий на вход ровно два аргумента — вещественные числа — и возвращающий также вещественное число
        """
        return operation(self.number1, self.number2)


c = Calculator(10, 3)

operations = (op.add, op.sub, op.mul, op.truediv, op.floordiv, op.pow)
for oper in operations:
    result = c.calculate(oper)
    print(result)
print()

# print(c.calculate(op.neg))
print(c.calculate(Calculator))
print(c.calculate(Calculator) == c)

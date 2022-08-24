bi_sum = __builtins__.sum

def sum(n1: float, n2: float, *numbers: float):
    """Переопределение встроенной функции sum() с возможностью передавать произвольное количество аргументов."""
    numbers += (n1, n2)
    return bi_sum(numbers)


res = sum(1, 2, 3, 4, 5)
print(res)

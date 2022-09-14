import numbers
import functools
import pprint


def hello():
    print('hello')

def cbrt(number: int):
    return pow(number, 1/3)

def adder(number1: int, number2: int):
    return number1 + number2

def product(number1: float, number2: float, *args: float):
    args = (number1, number2) + args
    return functools.reduce(lambda n1, n2: n1*n2, args)


funcs = {}
for name, obj in globals().copy().items():
    if not (name.startswith('__') and name.endswith('__')):
        if '__call__' in dir(obj):
            funcs[name] = obj

pprint.pprint(funcs)
print('\n')

# вызываем функции из словаря
# for func in funcs.values():
    # try:
        # сначала без аргументов
        # func()
    # except TypeError as e:
        # смотрим текст исключения
        # for ch in str(e):
            # if ch.isdecimal():
                # берём из текста количество обязательных аргументов
                # req_args = int(ch)
                # break
        # else:
            # req_args = 0
        # запрашиваем обязательные аргументы у пользователя
        # args = []
        # for i in range(req_args):
            # prompt = f' _ аргумент {i+1} для функции {func.__name__}: '
            # args += [int(input(prompt))]
        # повторно вызываем функцию
        # print(func(*args))


# вызываем функции из словаря
for func in funcs.values():
    args = []
    # итерируемся по объектам словаря __annotations__ для каждого объекта функции
    for arg_name, arg_type in func.__annotations__.items():
        prompt = (f' _ аргумент {arg_name} '
                  f'типа {arg_type.__name__} '
                  f'для функции {func.__name__}: ')
        # запрашиваем аргумент соответствующего типа:
        args += [arg_type(input(prompt))]
    # повторно вызываем функцию
    print(func(*args))


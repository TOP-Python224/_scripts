def calc(number1: float, 
         number2: float, 
         oper_sign: str) -> int | float:
    """Выполняет указанную арифметическую операцию с двумя числами."""
    if oper_sign == '+':
        return number1 + number2
    elif oper_sign == '-':
        return number1 - number2
    elif oper_sign == '*':
        return number1 * number2
    elif oper_sign == '/':
        return number1 / number2

while True:
    num1 = input('\n > введите первое число: ')
    if not num1:
        break
    else:
        num1 = int(num1)
    num2 = int(input(' > введите второе число: '))
    oper = input(' > введите знак математической операции: ')
    res = calc(num1, num2, oper)
    print(f'\t{res}')

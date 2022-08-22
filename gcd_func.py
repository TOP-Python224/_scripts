def gcd(number1: int, number2: int) -> int:
    """Возвращает наибольший общий делитель двух чисел."""
    number1 = max(number1, number2)
    number2 = min(number1, number2)
    while mod := number1 % number2:
        number1, number2 = number2, mod
    return number2


while True:
    n = input('\n > введите первое число: ')
    if not n:
        break
    else:
        n = int(n)
    m = int(input(' > введите второе число: '))
    print(f'\tgcd() = {gcd(n, m)}')

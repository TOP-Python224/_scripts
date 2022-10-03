
def adder(number: int):
    res = 0
    if number > 0:
        print(f'вызов\t{number = }\t{res = }')
        res += number + adder(number-1)
        print(f'возврат\t{number = }\t{res = }')
        return res
    else:
        print('конец рекурсии')
        return number


print(adder(5))

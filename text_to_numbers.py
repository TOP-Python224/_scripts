inp = input(' числа через пробел > ')
# stdin: 1 2 3.3 4 5.55 6.66 7
# stdin: abc def 3gh 4 5.5 6ij 7.q 8.8

def int_or_float_in_str(s: str) -> bool:
    s_without_point = s.replace('.', '')
    ret = s_without_point.isdecimal()
    return ret

str_nums = tuple(filter(
    # lambda s: s.replace('.', '').isdecimal(),
    int_or_float_in_str,
    inp.split()
))

numbers1 = map(float, str_nums)
print(list(numbers1))
# stdout: [1.0, 2.0, 3.3, 4.0, 5.55, 6.66, 7.0]

numbers2 = map(lambda s: float(s) if '.' in s else int(s), str_nums)
print(list(numbers2))
# stdout: [1, 2, 3.3, 4, 5.55, 6.66, 7]

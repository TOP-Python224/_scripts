# (
    # <выражение> 
    # for <переменная_цикла> in <итерируемый объект> 
    # if <условие_фильтрации> — опционально
# )

a = [n for n in range(10, 100, 10)]
b = {n for n in range(10, 100, 10)}
c = {n: n**2 for n in range(10, 100, 10)}
d = (n for n in range(10, 100, 10))

print(f'{type(a) = }')
print(f'{type(b) = }')
print(f'{type(c) = }')
print(f'{type(d) = }')

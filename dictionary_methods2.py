d = {1: 'a', 2: 'b'}

# прямое обращение к несуществующему ключу приводит к ошибке
# print(d[3])

for n in range(4):
    # если ключ n присутствует в словаре, то метод get() вернёт значение по этому ключу
    # иначе, вернёт объект None (по умолчанию)
    print(f"d.get({n}) = {d.get(n)!r}")
print()

for n in range(4):
    print(f"d.get({n}) = {d.get(n, '')!r}")


decims = {}
print('\n', decims, sep='', end='\n\n')
for n in range(10, 51, 10):
    # if n in decims:
        # decims[n] += 1
    # else:
        # decims[n] = 1
    # метод setdefault() 
    #   для несуществующего ключа создаёт элемент (ключ: значение-по-умолчанию) и возвращает значение (None по умолчанию)
    #   для существующего ключа вовзвращает текущее значение по этому ключу
    decims[n] = decims.setdefault(n, 0) + 1
    print(f"decims[{n}] = {decims.setdefault(n, 0)}")
print('\n', decims, sep='', end='\n\n')

for n in range(10, 100, 10):
    decims[n] = decims.setdefault(n, 0) + 1
    print(f"decims[{n}] = {decims.setdefault(n, 0)}")
print()

n = int(input('число: '))
flag = False

for i in range(1, n+1):
    for j in range(i):
        if j**2 % 10 == 4:
            print('переключение флага')
            flag = True
            break
    print('проверка флага')
    if flag:
        break


s = input('\nновая строка: ')

if s:
    print('не пустая строка')
else:
    print('пустая строка')


m = int(input('\nещё одно число: '))

if m // 100:
    print('трёхзначное число')
else:
    print('не трёхзначное число')

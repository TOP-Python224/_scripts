a, b = int(input('Число 1: ')), int(input('Число 2: '))

if a < b:
    print('Блок if')
    print(f'{a} меньше {b}')
elif a > b:
    print('Блок elif')
    print(f'{a} больше {b}')
else:
    print('Блок else')
    print(f'{a} равно {b}')

print('Конец условной конструкции')

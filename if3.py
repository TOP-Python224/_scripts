name1 = 'John'
age1 = 20

name2 = 'Viktor'
age2 = 30

name3 = 'ひろひと'
age3 = 40

if 25 <= age1 <= 50:
    if name1.isalpha():
        print(f'{name1} подходит')
    else:
        print('ошибка в имени')
else:
    print("не подходит по возрасту")

if 25 <= age2 <= 50:
    if name2.isalpha():
        print(f'{name2} подходит')
    else:
        print('ошибка в имени')
else:
    print("не подходит по возрасту")

if 25 <= age3 <= 50:
    if name3.isalpha():
        print(f'{name3} подходит')
    else:
        print('ошибка в имени')
else:
    print("не подходит по возрасту")



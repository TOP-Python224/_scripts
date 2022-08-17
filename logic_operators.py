# n = int(input('число: '))

# if -10 < n and n < 10:
    # print('однозначное целое')
# print()


# if (int(input('левая граница: ')) < n 
    # and n < int(input('правая граница: '))):
        # print('в диапазоне')
# else:
        # print('не в диапазоне')
# print()


# comm = input(' > ')

# if (comm == 'quit' 
    # or comm == 'exit'
    # or comm == 'выход' 
    # or comm == 'выйти'):
        # print('выход...')


# print('\nугадайка')
# if (n == int(input('n = ? '))
    # or n == int(input('n = ? '))
    # or n == int(input('n = ? '))
    # or n == int(input('n = ? '))):
        # print('угадал')
# else:
        # print('не угадал')


# if not n:
    # print('ноль')
# else:
    # print('не ноль')


# два способа записи одного и того же условного выражения
# if not '!' in comm:
# if '!' not in comm:
    # print('команда пользователя')
# else:
    # print('команда администратора')


# '' or 12 or True -> False or True or True
print(f"{'' or 12 or True = }")
print(f"{'' or 0 or True = }")
print(f"{'asd' or 0 or True = }")
print(f"{'' or 0 or 0.0 = }\n\n")

# True and 0 and 'asd' -> True or False or True
print(f"{True and 12 and 'asd' = }")
print(f"{False and 12 and 'asd' = }")
print(f"{True and 0 and 'asd' = }")
print(f"{True and 0 and '' = }")

def func(param):
    return param or 'error'

# 1. устаревший способ
msg = input(' > ')
# msg = ' '
while msg:
    print(f"\t{msg.upper()}")
    msg = input(' > ')

print('конец цикла\n')


# 2. для версии Python 3.8+
#   walrus operator — моржовый оператор
while msg := input(' > '):
    print(f"\t{msg.upper()}")

print('конец цикла\n')


# 3. условно-бесконечный цикл с дополнительными проверками
while True:
    msg = input(' > ')
    if msg:
        print(f"\t{msg.upper()}")
    else:
        break

print('конец цикла\n')

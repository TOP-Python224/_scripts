# одного ли цвета клетки?
# на вход программе поступают четыре строки:
# stdin:
#   a
#   1
#   b
#   3

# вариант 1
c1_v, c1_h = input(), int(input())
c2_v, c2_h = input(), int(input())

if c1_v == 'a': c1_v = 1
if c1_v == 'b': c1_v = 2
if c1_v == 'c': c1_v = 3
if c1_v == 'd': c1_v = 4
if c1_v == 'e': c1_v = 5
if c1_v == 'f': c1_v = 6
if c1_v == 'g': c1_v = 7
if c1_v == 'h': c1_v = 8

if c2_v == 'a': c2_v = 1
if c2_v == 'b': c2_v = 2
if c2_v == 'c': c2_v = 3
if c2_v == 'd': c2_v = 4
if c2_v == 'e': c2_v = 5
if c2_v == 'f': c2_v = 6
if c2_v == 'g': c2_v = 7
if c2_v == 'h': c2_v = 8

if (c1_v % 2 == 0 and c1_h % 2 == 0 and c2_v % 2 == 0 and c2_h % 2 == 0
    or c1_v % 2 == 0 and c1_h % 2 == 0 and c2_v % 2 != 0 and c2_h % 2 != 0
    or c1_v % 2 != 0 and c1_h % 2 != 0 and c2_v % 2 != 0 and c2_h % 2 != 0
    or c1_v % 2 != 0 and c1_h % 2 != 0 and c2_v % 2 == 0 and c2_h % 2 == 0):
        print('ДА')
else:
        print('НЕТ')


# вариант 2
c1_v, c1_h = ord(input()), int(input())
c2_v, c2_h = ord(input()), int(input())
# сумма чётного количества нечётных чисел всегда чётная
if (c1_v + c1_h + c2_v + c2_h) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')


# вариант 3
verticals = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 
    'e': 5, 'f': 6, 'g': 7, 'h': 8
}

c1_v, c1_h = verticals[input()], int(input())
c2_v, c2_h = verticals[input()], int(input())

if (c1_v + c1_h + c2_v + c2_h) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')



# сможет ли король переместиться с первой клетки на вторую за один ход?
# stdin:
#   a
#   1
#   b
#   3

c1_v, c1_h = ord(input()), int(input())
c2_v, c2_h = ord(input()), int(input())
if abs(c2_v - c1_v) <= 1 and abs(c2_h - c1_h) <= 1:
    print('ДА')
else:
    print('НЕТ')


# for i in range(5):
    # print(i)

# счётчик
cnt = 0
while cnt < 5:
    print(cnt)
    # оператор расширенного присваивания
    cnt += 1
    # cnt = cnt + 1


lm = int(input('левая граница: '))
rm = int(input('правая граница: '))
step = int(input('шаг последовательности: '))
# счётчик
cnt = lm
# тернарный оператор if...else
# <выражение-если-True> if <условие> else <выражение-если-False>
while cnt < rm if step > 0 else cnt > rm:
    print(cnt)
    cnt += step

# рука из пяти карт, только номиналы, J=11, Q=12, K=13, A=1
# найти самую старшую комбинацию в руке
    # старшая карта
    # пара
    # две пары
    # сет
    # стрит
    # фулл-хаус
    # каре

from random import randrange as rr

hand = ()
for _ in range(5):
    hand += (rr(1, 14),)
print(*hand, sep=', ')

unique = ()
for card in hand:
    if card not in unique:
        unique += (card,)
lu = len(unique)
# print(*unique, sep=', ')

comb = 'старшая карта'

if lu == 4:
    comb = 'пара'

if lu == 3:
    q = ()
    for card in unique:
        q += (hand.count(card),)
    if max(q) == 2:
        comb = 'две пары'
    else:
        comb = 'сет'

if lu == 5:
    q = sorted(unique)
    if q == list(range(q[0], q[0]+5)):
        comb = 'стрит'

if lu == 2:
    for card in unique:
        q += (hand.count(card),)
    if max(q) == 3:
        comb = 'фулл-хаус'
    else:
        comb = 'каре'

if lu == 1:
    print('Шулер!')


print(comb)

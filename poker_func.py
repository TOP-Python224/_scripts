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

# переменные типов для аннотации
CardHand = tuple[int, int, int, int, int]

def checkhand(hand: CardHand) -> str:
    """Возвращает название самой старшей покерной комбинации в кортеже из пяти карт.
    
    Используются комбинации техасского холдема."""
    unique = ()
    for card in hand:
        if card not in unique:
            unique += (card,)
    lu = len(unique)
   
    if lu == 5:
        q = sorted(unique)
        if q == list(range(q[0], q[0]+5)):
            comb = 'стрит'
        else:
            return 'старшая карта'
   
    if lu == 4:
        return 'пара'
    
    if lu == 3:
        q = ()
        for card in unique:
            q += (hand.count(card),)
        if max(q) == 2:
            return 'две пары'
        else:
            return 'сет'
    
    if lu == 2:
        for card in unique:
            q += (hand.count(card),)
        if max(q) == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    
    if lu == 1:
        return 'Шулер!'


hand = ()
for _ in range(5):
    hand += (rr(1, 14),)
print(*hand, sep=', ')
print(checkhand(hand))

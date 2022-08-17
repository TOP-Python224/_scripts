from random import randrange as rr

combinations = ('старшая карта', 'пара', 'две пары', 'сет', 'стрит', 'фулл-хаус', 'каре')
comb_rates = ()

N = 1000

for c in combinations:
    cnt = 0
    for _ in range(N):
        comb = 'старшая карта'
        while comb != c:
            hand = ()
            for _ in range(5):
                hand += (rr(1, 14),)
            cnt += 1
            
            unique = ()
            for card in hand:
                if card not in unique:
                    unique += (card,)
            lu = len(unique)

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
    
    comb_rates += (round(cnt / N, 1), )

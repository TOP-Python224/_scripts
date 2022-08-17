dictionary1 = {'a': 1, 'b': 2}

dictionary2 = dict([(12, 'first'), 
                    (0.98, 'second'), 
                    ('key', False)])

dictionary3 = dict(key1=0.01, key2=0.02, key3=0.03)

l = range(10, 100, 10)
dictionary4 = dict.fromkeys(l, '')

l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
# print(*zip(l1, l2), sep='\n')
dictionary5 = dict(zip(l1, l2))

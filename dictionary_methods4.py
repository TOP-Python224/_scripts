d = {12: 'c', ('ab', 103): [1, 2, 3], 'xyz': 0.0123}

# список тех ключей словаря, которые необходимо оставить - другие ключи словаря должны быть удалены
l = [12, 'xyz']

for key in list(d):
    if key not in l:
        d.pop(key)
print(d)

# {12: 'c', 'xyz': 0.0123}

for _ in range(3):
    print(d.popitem())

from random import randrange as rr

# литерал множества
s1 = {1, 2, 3, 1, 4, 5}
print(f'{s1 = }\n{type(s1) = }\n')


decimals = range(10, 100, 10)
rand_nums = [rr(11, 20) for _ in range(20)]

print(f'{decimals = }\n{type(decimals) = }\n')
print(f'{rand_nums = }\n{type(rand_nums) = }\n')

# преобразования итерируемых объектов во множества
s2 = set(decimals)
s3 = set(rand_nums)

print(f'{s2 = }\n')
print(f'{s3 = }\n\n')


fs1 = frozenset((1, 4, 'a', 0.01))
print(f'{fs1 = }\n{type(fs1) = }\n')

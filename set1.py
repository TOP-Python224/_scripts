from random import randrange as rr

s1 = {1, 2, 3, 1, 4, 5}
print(f'{s1 = }\n{type(s1) = }\n')

decimals = range(10, 100, 10)
print(f'{decimals = }\n{type(decimals) = }\n')

s2 = set(decimals)
print(f'{s2 = }\n{type(s2) = }\n')

rand_nums = [rr(11, 20) for _ in range(20)]
print(f'{rand_nums = }\n{type(rand_nums) = }\n')

s3 = set(rand_nums)
print(f'{s3 = }\n{type(s3) = }\n\n')


fs1 = frozenset((1, 4, 'a', 0.01))
print(f'{fs1 = }\n{type(fs1) = }\n')

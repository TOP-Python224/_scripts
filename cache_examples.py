from functools import lru_cache
from random import randrange as rr


@lru_cache(maxsize=1)
def return_rand(a: int, b: int):
    return rr(a, b+1)


print(return_rand(10, 99))
print(return_rand(10, 99))
print(return_rand(10, 99))
print(return_rand(10, 99))

print(return_rand(100, 999))
print(return_rand(100, 999))
print(return_rand(100, 999))
print(return_rand(100, 999))

print(return_rand(10, 99))
print(return_rand(10, 99))
print(return_rand(10, 99))
print(return_rand(10, 99))

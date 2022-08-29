from typing import Callable, Any
from time import perf_counter_ns as pc_ns
from random import randrange as rr


def timer(func_obj: Callable, *args, **kwargs) -> tuple[Any, int]:
    """Засекает время, необходимое для вызова функции func_obj.

    Возвращает в кортеже результат функции func_obj и затраченное на вызов время."""
    start = pc_ns()
    ret = func_obj(*args, **kwargs)
    end = pc_ns()
    time = end - start
    return ret, time


# тестовые функции
def list_generate(limit: int):
    return [rr(10) for _ in range(limit)]

def set_generate(limit: int):
    return {rr(10) for _ in range(limit)}


N = 10**6

t1 = timer(list_generate, N)[1]
t2 = timer(set_generate, N)[1]

print(f'{N = }')
print(f'генерация списка: {t1} нс')
print(f'генерация множества: {t2} нс')

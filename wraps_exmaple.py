from functools import wraps


def decorator(func_obj):
    @wraps(func_obj)
    def _wrapper(*args, **kwargs):
        print('декоратор начинает')
        r = func_obj(*args, **kwargs)
        print('декоратор заканчивает')
        return r
    return _wrapper



def test_func(arg1: str):
    """Функция для проверки декоратора wraps."""
    return arg1*2
test_func = decorator(test_func)


print(test_func.__name__)
print(test_func.__doc__)
print(test_func.__annotations__)

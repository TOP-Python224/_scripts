def test_func() -> None:
    """Выводит тестовую строку в stdout."""
    print('test_func: вызов функции')

print(f'{test_func = }')
print(f'{type(test_func) = }')
print(f'{test_func.__name__ = }')
print(f'{test_func.__doc__ = }')
print(f'{test_func() = }\n\n')


def test_func2() -> str:
    """Возвращает тестовую строку."""
    return 'test_func:' + ' вызов функции'

print(f'{test_func2 = }')
print(f'{type(test_func2) = }')
print(f'{test_func2.__name__ = }')
print(f'{test_func2.__doc__ = }')
print(f'{test_func2() = }\n\n')


globs = globals().copy()
for name, obj in globs.items():
    if '__call__' in dir(obj):
        print(obj.__name__)
        print('\t' + str(obj.__annotations__))
        print('\t' + obj.__doc__, end='\n\n')

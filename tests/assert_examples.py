from string import ascii_lowercase, whitespace


assert 3 == 3
print('Тест 1 пройден')


try:
    assert 3 == 3 / 10
except AssertionError:
    print('Тест 2 провален')
else:
    print('Тест 2 пройден')


try:
    assert 3 == 3 / 0
except AssertionError:
    print('Тест 3 провален')
except ZeroDivisionError as e:
    print(f'Тест 3 провален: {e}')
else:
    print('Тест 3 пройден')



class A:
    def __init__(self):
        self.data = input(' > ').lower().strip()

    @staticmethod
    def valid_input(data: str):
        return set(data) <= set(ascii_lowercase) | set(whitespace)


a = A()

assert a.valid_input(a.data), 'string should contain only latin letters and space characters'
print("Тест 4 пройден")

assert 2 < len(a.data) < 10, 'length of string should be between 3 and 9 characters'
print("Тест 5 пройден")


def get_divisors(number: int) -> list[int]:
    result = []
    if number == 0:
        return result
    for div in range(abs(number)//2 + 1, 0, -1):
        if number % div == 0:
            result += [div]
    return [number] + result


# данные для тестов
zero = 0
prime = 19
positive = 6
negative = -12


def test_divisors_zero():
    assert get_divisors(zero) == []


def test_divisors_prime():
    assert len(get_divisors(prime)) == 2


def test_divisors_positive():
    assert len(get_divisors(positive)) > 2


def test_divisors_negative():
    assert len(get_divisors(negative)) > 2


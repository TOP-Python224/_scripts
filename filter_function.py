from typing import Callable, Iterable
from random import randrange as rr


def myfilter(predicate: Callable, iterator: Iterable):
    ret = []
    for elem in iterator:
        if predicate(elem):
            ret += [elem]
    return ret


def is_prime(obj) -> bool:
    for n in range(2, obj//2 + 1):
        if obj % n == 0:
            return False
    else:
        return True

def is_match_exception(obj) -> bool:
    tld = obj % 100
    return True if tld in range(11, 15) else False


data_test = [rr(10, 200) for _ in range(50)]
ret_test = myfilter(is_prime, data_test)
filter_test = filter(is_prime, data_test)

print(ret_test)
print(list(filter_test), end='\n\n')

ret_test = myfilter(is_match_exception, data_test)
print(ret_test, end='\n\n')


def hour_end(hours: int) -> str:
    ld = hours % 10
    if ld in (0, 5, 6, 7, 8, 9) or is_match_exception(hours):
        return 'ов'
    elif ld in (2, 3, 4):
        return 'а'
    else:
        return ''

def minute_end(minutes: int) -> str:
    ld = minutes % 10
    if ld in (0, 5, 6, 7, 8, 9) or is_match_exception(minutes):
        return ''
    elif ld in (2, 3, 4):
        return 'ы'
    else:
        return 'а'

minutes_input = int(input(' минуты > '))
hour, minute = divmod(minutes_input, 60)
print(f"{minutes_input} минут{minute_end(minutes_input)}"
      f" — {hour} час{hour_end(hour)}"
      f" {minute} минут{minute_end(minute)}")

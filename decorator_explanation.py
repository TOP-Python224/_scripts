from time import perf_counter as pc
from time import perf_counter_ns as pc_ns
from typing import Callable
from time import sleep


def rounder(number: float, meaning_digits: int = 2) -> float:
    if abs(number) >= 1:
        return round(number, meaning_digits)
    elif 0 < abs(number) < 1:
        for exp in range(1, 16):
            if int(number * 10**exp) >= 1:
                return round(number, exp+meaning_digits-1)


def time_elapser(function_object: Callable):
    """Декоратор. Засекает и выводит в stdout время выполнения декорируемой функции."""
    def _wrapper(*args, **kwargs):
        """Подменяет объект декорируемой функции."""
        # начало работы таймеров
        start_s = pc()
        start_ns = pc_ns()
        # вызов декорируемой функции и сохранение её возвращаемого значения
        ret = function_object(*args, **kwargs)
        # отсечка таймеров
        end_ns = pc_ns()
        end_s = pc()
        # продолжительность работы таймеров
        period_s = end_s - start_s
        period_ns = end_ns - start_ns
        # сообщение в stdout
        print(f' _ elapsed time for {function_object.__name__}():'
              f' {rounder(period_s)} s ({period_ns} ns)')
        # возврат результата декорируемой функции
        return ret
    # возврат объекта функции для подмены декорируемой функции
    return _wrapper


# @time_elapser — синтаксический сахар для декорирования функций
def test_func():
    """Ничего не делает в течение 0.5 секунд."""
    sleep(0.5)

# декорирование функции
test_func = time_elapser(test_func)

test_func()

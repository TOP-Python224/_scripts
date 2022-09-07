from typing import Callable
from time import sleep
from random import choice


def repeat_connection(func_obj: Callable) -> Callable:
    def _wrapper(*args, **kwargs):
        print('...подключение к серверу')
        res = func_obj(*args, **kwargs)
        if res is None:
            print('...ошибка сети')
            sleep(2)
            print('...подключение к серверу')
            res = func_obj(*args, **kwargs)
            if res is None:
                print('...ошибка сети')
                print('...проверьте настройки сети')
            else:
                print('...подключение успешно')
        else:
            print('...подключение успешно')
    return _wrapper


@repeat_connection
def connect_server(url: str):
    return choice([None, True, False])


connect_server('http://yahoo.com')

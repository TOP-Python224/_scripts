from datetime import datetime as dt
from time import sleep


class Logger:
    """Класс для ведения и формирования лог-файлов."""
    def __init__(self):
        self.__entries: list[str] = []

    @property
    def entry(self):
        """Предотвращает возможность чтения записей объекта журнала во время выполнения программы."""
        return None
        # raise NotImplementedError('access denied')

    # сеттер добавляет элемент в список, но в коде верхнего уровня это выглядит как перезапись поля entry — нежелательный вариант реализации сеттера
    @entry.setter
    def entry(self, value: str):
        self.__entries += [f'{dt.now():%Y-%m-%d %H:%M:%S} — {value}\n']

    def to_file(self) -> None:
        with open('journal.log', 'w', encoding='utf-8') as fileout:
            fileout.writelines(self.__entries)


journal = Logger()

journal.entry = 'first entry'
sleep(1.5)
journal.entry = 'top secret data'
sleep(0.83)
journal.entry = 'this should be dumped to a file'

journal.to_file()
print(journal.entry)

"""Single Responsibility Principle — Принцип Единственной Ответственности"""

from datetime import datetime as dt
from pathlib import Path
from sys import path


class Journal:
    """
    Позволяет добавлять и хранить текстовые сообщения с отметками времени добавления.
    """
    def __init__(self):
        self.history: list = []

    def add_entry(self, msg: str):
        self.history += [(dt.now(), msg)]

    def __str__(self):
        return '\n'.join(
            f'{ts:%Y-%m-%d %H:%M:%S} — {msg}'
            for ts, msg in self.history
        )

    # является нарушением SRP
    # def to_file(self, file_path: str | Path):
    #     with open(file_path, 'a+', encoding='utf-8') as fileout:
    #         fileout.write(str(self))


class FileSystemManager:
    """
    Предоставляет пути и методы для чтения/записи в объекты файловой системы.
    """
    script_dir: str | Path = Path(path[0])
    default_journal_path: str | Path = script_dir / (str(Path(__file__).stem) + '_journal.log')

    @classmethod
    def file_append_entries(cls, data: str, file_path: str | Path = None):
        if not file_path:
            file_path = cls.default_journal_path
        with open(file_path, 'a+', encoding='utf-8') as fileout:
            fileout.write(data + '\n')


j = Journal()
j.add_entry(input(' > '))
j.add_entry(input(' > '))

FileSystemManager.file_append_entries(str(j))

from datetime import datetime as dt
from pathlib import Path


PROJECT_DIR = Path(r'D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\224\scripts\tests\project')
DATA_DIR = PROJECT_DIR / 'data'
LOG_DIR = PROJECT_DIR / 'logs'


class Logger:
    default_log_path: str | Path = LOG_DIR / f'{dt.now():%Y-%m-%d}.log'

    @classmethod
    def append_log(cls, data: str, log_path: str | Path = None):
        if not log_path:
            log_path = cls.default_log_path
        with open(log_path, 'a', encoding='utf-8') as fileout:
            fileout.write(f'{dt.now():%Y-%m-%d %H:%M:%S} — {data}\n')


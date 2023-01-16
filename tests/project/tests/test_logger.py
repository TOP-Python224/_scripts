from datetime import datetime as dt
from json import load as jload
from pathlib import Path
from pytest import fixture

from source import logger


@fixture
def conffile_path():
    return Path(r'D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\224\scripts\tests\project\data\conf.json')


@fixture
def datafile_path(conffile_path):
    with open(conffile_path, encoding='utf-8') as filein:
        data = jload(filein)
    return Path(data['paths']['data']) / 'test/log_file.json'


@fixture
def data(datafile_path):
    with open(datafile_path, encoding='utf-8') as filein:
        data = jload(filein)
    return data


@fixture
def filename_format(data):
    return data['filename_format']


@fixture
def timestamp_format(data):
    return data['timestamp_format']


@fixture
def content(data):
    return data['content']


def test_log_exists(filename_format):
    logger.Logger.append_log('')
    filename = f'{dt.now():{filename_format}}.log'
    assert (logger.LOG_DIR / filename).is_file()
    (logger.LOG_DIR / filename).unlink()


def test_log_content(filename_format, timestamp_format, content):
    logger.Logger.append_log(content)
    filename = f'{dt.now():{filename_format}}.log'
    data = (logger.LOG_DIR / filename).read_text(encoding='utf-8')
    assert data.strip() == f'{dt.now():{timestamp_format}} — {content}'
    (logger.LOG_DIR / filename).unlink()


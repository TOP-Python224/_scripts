"""Более безопасный и более удобный в использовании код подключения к БД."""

from csv import reader
from decimal import Decimal as dec
from json import load as jload
from mysql.connector import connect, DatabaseError
from pathlib import Path
from sys import path
from time import sleep


DIR_PATH = Path(path[0])


dbconfig_path = DIR_PATH / 'dbconfig.json'
with open(dbconfig_path, encoding='utf-8') as filein:
    dbconfig = jload(filein)


script_path = DIR_PATH / 'hospital/create.sql'
script = script_path.read_text(encoding='utf-8')

data_path = DIR_PATH / 'hospital/insert.csv'
with open(data_path, encoding='utf-8') as filein:
    data = list(reader(filein))

for i in range(len(data)):
    for j in range(2,4):
        data[i][j] = dec(data[i][j])

insert = (
    "insert into `doctors`"
    "  (`name`, `surname`, `salary`, `premium`)"
    "values"
    "  (%s, %s, %s, %s)"
)

with connect(**dbconfig) as conn:
    conn.autocommit = True

    with conn.cursor() as cur:
        try:
            cur.execute(script, multi=True)
        except DatabaseError as exc:
            print(f'DB server internal error: {exc.errno}')
            print(f'{exc}')

    sleep(0.25)

    conn.reconnect()
    conn.database = 'hospital'

    with conn.cursor() as cur:
        try:
            cur.executemany(insert, data)
        except DatabaseError as exc:
            print(f'DB server internal error: {exc.errno}')
            print(f'{exc}')


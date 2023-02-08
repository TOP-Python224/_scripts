"""Более безопасный и более удобный в использовании код подключения к БД."""

from json import load as jload
from mysql.connector import connect
from pathlib import Path
from sys import path


dbconfig_path = Path(path[0]) / 'dbconfig.json'
with open(dbconfig_path, encoding='utf-8') as filein:
    dbconfig = jload(filein)

join_countries_capitals = (
    "select `country`.`Name` as 'Country',\n"
    "	     `city`.`Name` as 'Capital'\n"
    "  from `country`\n"
    "  join `city`\n"
    "    on `country`.`Capital` = `city`.`ID`"
)

with connect(**dbconfig, database='world') as conn:
    with conn.cursor() as cur:
        cur.execute(join_countries_capitals)
        column_names = cur.column_names
        data = cur.fetchall()

print(column_names)
for row in data:
    print(row)


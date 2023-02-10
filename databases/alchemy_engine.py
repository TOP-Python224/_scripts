from json import load as jload
from pathlib import Path
from re import fullmatch
from sqlalchemy import create_engine, text
from sys import path


# шаблон строки для подключения к БД:
# dialect[+driver]://user:password@host[:port]/dbname[?key=value..]

# пример того, как может выглядеть строка для подключения к конкретной БД
mysql_url = 'mysql+mysqlconnector://root:root@127.0.0.1:3300'

# чтение конфиденциальных данных
dbconfig_path = Path(path[0]) / 'dbconfig_alchemy.json'
with open(dbconfig_path, encoding='utf-8') as filein:
    dbconfig: dict = jload(filein)

# формирование строки подключения для создания объекта движка
dialect = 'mysql'
mysql_url = (
    f"{dialect}"
    f"+{dbconfig[dialect]['dbapi']}"
    f"://{dbconfig[dialect]['user']}"
    f":{dbconfig[dialect]['password']}"
    f"@{dbconfig[dialect]['host']}"
    f":{dbconfig[dialect]['port']}"
    + (f"/{dbname}" if (dbname := dbconfig[dialect].get('database', '')) else '')
)

# создание объекта движка
engine = create_engine(mysql_url)

# изучение публичных атрибутов объекта движка
# for attr in dir(engine):
#     if not fullmatch(r'_{1,2}\w+(_{2})?', attr):
#         value = getattr(engine, attr)
#         print(f"{attr}\n\t{type(value)}\n\t{value}\n")

# предобработка текста SQL запросов
use_academy = text("use academy")
select_academy_faculties = text("select * from faculties")

use_world = text("use world")
select_world_capitals = text(
    "select `country`.`Name` as 'Country',\n"
    "	   `city`.`Name` as 'Capital'\n"
    "  from `country`\n"
    "  join `city`\n"
    "    on `country`.`Capital` = `city`.`ID`;\n"
)

# работа с объектом подключения
with engine.connect() as conn:
    conn.execute(use_academy)
    # метод execute() возвращает курсор
    cursor = conn.execute(select_academy_faculties)
    # извлекаем данные из курсора
    faculties = cursor.fetchall()

    conn.execute(use_world)
    cursor = conn.execute(select_world_capitals)
    capitals = cursor.fetchall()


for row in faculties:
    print(row)
print('\n\n')

for row in capitals:
    print(row)
print('\n\n')


dialect = 'postgresql'
postgresql_url = (
    f"{dialect}"
    f"+{dbconfig[dialect]['dbapi']}"
    f"://{dbconfig[dialect]['user']}"
    f":{dbconfig[dialect]['password']}"
    f"@{dbconfig[dialect]['host']}"
    f":{dbconfig[dialect]['port']}"
    + (f"/{dbname}" if (dbname := dbconfig[dialect].get('database', '')) else '')
)
engine = create_engine(postgresql_url)

select_aircrafts = text("select * from bookings.aircrafts")

with engine.connect() as conn:
    cur = conn.execute(select_aircrafts)
    column_names = tuple(cur.keys())
    data = cur.fetchall()

print(column_names)
for row in data:
    print(row)

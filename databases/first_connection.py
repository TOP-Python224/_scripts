"""Простой, но небезопасный и неудобный для широкого использования код подключения к БД."""

from mysql.connector import connect
from pprint import pprint


connection = connect(
    host='127.0.0.1',
    port=3300,
    user='root',
    password='root',
    database='academy',
)

cursor = connection.cursor()

select_departments = """select * from `departments`"""

cursor.execute(select_departments)
# первый способ извлечения результирующих данных
data = cursor.fetchall()

cursor.execute(select_departments)
# второй способ извлечения результирующих данных
data = []
for row in cursor:
    data += [row]

cursor.close()

print(cursor.column_names)
pprint(data)


print('\n')


connection.database = 'hospital'
cursor = connection.cursor()

select_doctors = """select * from `doctors`"""

cursor.execute(select_doctors)
print(cursor.column_names)
for row in cursor:
    print(row)

cursor.close()
connection.close()

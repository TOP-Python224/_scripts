from datetime import datetime as dt

date1 = dt(2000, 10, 4)
print(date1)

now = dt.now()
print(now)

td1 = now - date1
print(td1)

while True:
    inp = input('\n > ')
    if not inp:
        break
    date2 = dt.strptime(inp, '%d.%m.%Y')
    print(f'{date2:%d %B %Y}')

posix_datetime = dt.now().timestamp()
print(posix_datetime)

date3 = dt.fromtimestamp(posix_datetime)
datetime_format = '%H:%M:%S %d %B %Y'
print(f'{date3:{datetime_format}}')

from sys import path
from pprint import pprint

script_dir = path[0]

cycles_file = '\\'.join((script_dir, 'cycles.txt'))

cycles_text = ''
n, m = int(input(' n > ')), int(input(' m > '))
for i in range(n):
    for j in range(m):
        cycles_text += f'{i = }\t{j = }\n'
    cycles_text += '\n'
cycles_text = cycles_text.strip()

with open(cycles_file, 'w', encoding='utf-8') as f_out:
    f_out.write(cycles_text)


with open(cycles_file, encoding='utf-8') as f_in:
    cycles_lines = f_in.readlines()

pprint(cycles_lines)

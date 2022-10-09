from pathlib import Path
from sys import path

from csv import writer, reader


script_dir = Path(path[0])
csv_path = script_dir / 'csv_example.csv'

with open(csv_path, 'w', encoding='utf-8') as f_out:
    csv_writer = writer(f_out)
    csv_writer.writerow(['1', '2', '3', '4', '5'])
    csv_writer.writerows(
        [('0.1', '0.2', '0.3', '0.4', '0.5'),
         ('ab', 'bc', 'cd', 'de', 'ef'),]
    )


with open(csv_path, encoding='utf-8') as f_in:
    csv_reader = reader(f_in)
    lines = list(csv_reader)

print(lines)

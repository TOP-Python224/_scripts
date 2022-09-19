from sys import path

script_dir = path[0]
hw_path = '\\'.join((script_dir, 'HW.txt'))

f_in = open(hw_path, encoding='utf-8')
hw_text = f_in.read()
f_in.close()

print(hw_text)


with open(hw_path, 'w', encoding='utf-8') as f_out:
    f_out.write('Тестовая запись')


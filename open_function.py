from sys import path

script_dir = path[0]
hw_path = '\\'.join((script_dir, 'HW.txt'))

f_in = open(hw_path, encoding='utf-8')

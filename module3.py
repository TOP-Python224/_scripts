"""Третий модуль программы демонстратора работы с модулями."""
print('начало выполнения модуля 3')

from module2 import M1_VAR, M2_VAR

from pprint import pprint


M3_VAR = 300

print(M1_VAR + M2_VAR + M3_VAR)

print('конец выполнения модуля 3')

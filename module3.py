"""Третий модуль программы демонстратора работы с модулями."""

print('начало выполнения модуля 3')

# импорт объектов осуществляется по ссылке
from module2 import M1_VAR, M2_VAR

import module2


M3_VAR = 300

print(f'\n{M1_VAR = }\n{M2_VAR = }\n{M3_VAR = }')

# объект в пространстве имён модуля 2 перезаписывается, и теперь имена module2.M2_VAR и M2_VAR (в прострастве имён модуля 3) ссылаются на разные объекты
module2.M2_VAR = 250
print(f'\n{module2.M2_VAR = }\n{M2_VAR = }')


module2.new_obj = []
module2.new_obj.append(222)

# импорт объекта осуществляется по ссылке
from module2 import new_obj

# изменяемый объект
print(f'\n{module2.new_obj = }\n{new_obj = }')

# объект изменяется, но не перезаписывается
module2.new_obj.append(233)
# ссылочная зависимость сохраняется
print(f'\n{module2.new_obj = }\n{new_obj = }')


# объект перезаписывается
module2.new_obj = [222, 233, 244]
# ссылочная зависимость разрывается
print(f'\n{module2.new_obj = }\n{new_obj = }\n')


print('конец выполнения модуля 3')

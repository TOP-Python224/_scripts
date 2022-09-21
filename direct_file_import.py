from pathlib import Path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec


script_dir = Path(path[0])
module_path = script_dir / '1.py'

# создание спецификации модуля
spec = spec_from_file_location('digit_name_module', module_path)
# создание объекта модуля
dmod = module_from_spec(spec)
# добавление в системный словарь элемента с именем и объектом модуля
modules['digit_name_module'] = dmod
# выполнение модуля
spec.loader.exec_module(dmod)


print(f'\n{dmod = }\n')

print(dmod.__name__)
print('\t'+ dmod.__doc__)

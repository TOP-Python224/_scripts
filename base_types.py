# преимущество динамической типизации
var = 10
var = 'abc'

# типы данных
print('типы данных')
print(f'объект {1}\t{type(1)}')
print(f'объект {True}\t{type(True)}')
print(f'объект {0.11}\t{type(0.11)}')
print(f'объект {1+1j}\t{type(1+1j)}')
print(f'объект {"aBc"}\t{type("aBc")}\n')

# преобразование в тип int
print('преобразование в тип int')
print(f"int(1.11) = {int(1.11)}")
print(f"{int(True) = }\t{int(False) = }")
print(f"{int(2.99) = }")
print(f"{int('3')}")
print(f"{int('-4')}\n")
# приводит к ошибке
# print(f"{int('5a') = }")

# преобразование в тип bool
print('преобразование в тип bool')
print(f"{bool(123) = }\t{bool(0) = }\t\t{bool(-3) = }")
print(f"{bool(0.0001) = }\t{bool(0.0) = }\t{bool(-1.3) = }")
print(f"{bool('False') = }\t{bool('') = }\t{bool('-100') = }\n")

# преобразование в тип float
print('преобразование в тип float')
print(f"{float(1) = }")
print(f"{float(True) = }\t{float(False) = }")
print(f"{float('2') = }")
print(f"{float('3.3') = }")
print(f"{float('-4.4') = }\n")
# приводит к ошибке
# print(f"{float('5h5') = }")

# преобразование в тип str
print('преобразование в тип str')
print(f"{str(1) = }")
print(f"{str(True) = }\t{str(False) = }")
print(f"{str(2.2) = }")
print(f"{str(3+3j) = }\n")

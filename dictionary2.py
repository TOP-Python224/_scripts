data = [
    {'p1': (1, 3, 6),
     'p2': (2, 4)},
    {'p1': (2, 3, 5),
     'p2': (1, 8, 9)},
]

# data_parsed = [
#   ['VAL', 'VAL', 'VAL', 'VAL', '', 'VAL', '', '', '']
#   ['VAL', 'VAL', 'VAL', '', 'VAL', '', '', 'VAL', 'VAL']
# ]

data_parsed = []
# перебор словарей в исходных данных
for i in range(len(data)):
    # создание списка-заготовки
    data_parsed += [['']*9]
    
    # создание итератора, включающего в себя все вложенные элементы значений словаря
    marked = ()
    for seq in data[i].values():
        marked += tuple(seq)
    
    # итерирование списка-заготовки
    for j in range(9):
        if j+1 in marked:
            data_parsed[i][j] = 'VAL'

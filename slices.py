from itertools import zip_longest

text = 'Python is cool!'
# длина последовательности — количество элементов последовательности -> int
text_length = len(text)
print(f"{text = }\t{text_length = }\n")

# срез
print(f"{text[7:9] = }")
# левая и правая границы срезов могут быть опущены — в таком случае срез 
#   берётся с начала или до конца
print(f"text[0:6] = {text[:6] = }")
print(f"text[10:15] = {text[10:] = }")
print(f"text[0:15] = {text[:] = }\n")

# срезы могут использовать несуществующие для текущей последовательности индексы
print(f"{text[12:17] = }")
print(f"{text[18:20] = }\n")

text2 = 'slices'
text2_length = len(text2)
print(f"{text2 = }\t{text2_length = }\n")

# проитерировать элементы нескольких последовательностей разной длины
for i in range(max(text_length, text2_length)):
    # приведёт к ошибке
    # print(f"{text[i]}\t{text2[i]}")
    print(f"{text[i:i+1]}   {text2[i:i+1]}")
print()

# альтернативный способ решения той же задачи
for elem1, elem2 in zip_longest(text, text2, fillvalue=''):
    print(f"{elem1}   {elem2}")
print()

# вывод положительных и торицательных индексов
for i in range(-text2_length, 0):
    print(i, end=' ')
print()
for i in range(text2_length):
    print(text2[i], end='  ')
print()
for i in range(text2_length):
    print(i, end='  ')
print('\n')

# срезы могут использовать отрицательную индексацию
print(f"{text2[-3:-1] = }")
print(f"{text2[-3:-5] = }")
print(f"{text2[-3:] = }")
# смешивание положительной и отрицательной индексации
print(f"{text2[1:-1] = }")
print(f"{text2[-4:5] = }\n")

# срезы могут использовать шаг взятия индексов
print(f"{text2[1:6:2] = }")
print(f"{text2[::3] = }")
print(f"{text2[::-1] = }")
print(f"{text2[-3:-5:-1] = }")
print(f"{text2[6:-6:-2] = }\n")

# print(f"{id(text) = }")
# print(f"{id(text[:]) = }")
# print(f"{text is text[:] = }\n")

print(f"{id(text) = }")
print(f"{id(text[2:5]) = }")
print(f"{text is text[2:5] = }")

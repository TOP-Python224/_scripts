text = 'Python is cool!'
# длина последовательности — количество элементов последовательности -> int
text_length = len(text)
print(f"{text = }\t{text_length = }")

print(f"{text[0] = }")
print(f"{text[1] = }")
print(f"{text[2] = }\n")
# приведёт к ошибке: IndexError
# print(f"{text[20] = }\n")

a = 3
b = 5

# в качестве индекса передаётся выражение, возвращающее int
print(f"{text[a] = }")
print(f"{text[b] = }")
print(f"{text[b - a] = }")
print(f"{text[int(input('index > '))] = }\n")

# i, j, k — имена переменных, которые принято использовать только для индексов
for i in range(-text_length, 0):
    print(i, end=' ' if i < -9 else '  ')
print()

for i in range(text_length):
    print(text[i], end='   ')
print()

for i in range(text_length):
    print(i, end='   ' if i < 10 else '  ')
print()

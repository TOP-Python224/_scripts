text = input(' > ')

print('\nУникальные символы из введённой строки')
for char in set(text):
    print(char, end=', ')
print('\n')

unique_chars = set(text)

while True:
    char = input(' > ')
    if not char:
        break
    if char in unique_chars:
        print(f"'{char}' находится в множестве")
    else:
        print(f"'{char}' отсутствует в множестве")

q = {list(text)}

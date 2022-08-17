from pprint import pprint

l = range(10, 100, 10)
decims = dict.fromkeys(l, '')

print(f"{type(decims)}\t{decims = }\n")
# приведёт к исключению KeyError
# print(f"{decims['b'] = }\n")

# добавит элемент в словарь
decims[-10] = ''
for d in range(-20, -100, -10):
    decims[d] = ''

decims[-90] = 'minus ninty'
for key in decims:
    if key < 0:
        decims[key] = 'minus '

for d in (10, -10):
    decims[d] += 'ten'
for d in (20, -20):
    decims[d] += 'twenty'
for d in (30, -30):
    decims[d] += 'thirty'
for d in (40, -40):
    decims[d] += 'fourty'
for d in (50, -50):
    decims[d] += 'fifty'
for d in (60, -60):
    decims[d] += 'sixty'
for d in (70, -70):
    decims[d] += 'seventy'
for d in (80, -80):
    decims[d] += 'eighty'
for d in (90, -90):
    decims[d] += 'ninty'

pprint(decims)

phrase = input('phrase: ')

if '?' in phrase:
    print("it's a question")
elif '!' in phrase:
    print("it's an exlamation")
elif '...' in phrase:
    print("it's a phrase with multi-dot")
print()

text = phrase
print(f"{id(phrase) = }")
print(f"{id(text) = }")

if id(phrase) == id(text):
    print('same object')

if phrase is text:
    print('same object')
else:
    print('different objects')

q = 'abcd'
if q is phrase:
    print('same object')
else:
    print('different objects')

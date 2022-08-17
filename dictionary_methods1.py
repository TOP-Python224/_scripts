from pprint import pprint

dict1 = dict([(12, 'first'), 
              (0.98, 'second'), 
              ('key', False)])


print(dict1.keys(), type(dict1.keys()))
print(*dict1.keys())

for key in dict1.keys():
    pass

for key in dict1:
    pass

# при итерации по объекту словаря применяется метод keys()
# print(list(dict1.keys()))
print(list(dict1), end='\n\n')


print(dict1.values(), type(dict1.values()))
print(*dict1.values())
print(list(dict1.values()), end='\n\n')


print(dict1.items(), type(dict1.items()))
print(*dict1.items())
print(list(dict1.items()), end='\n\n')


dict1_inv = {}
for key, value in dict1.items():
    dict1_inv[value] = key
print(dict1_inv)

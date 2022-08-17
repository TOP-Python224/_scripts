data = [1, 4, 2, 6, 3, 5, 1, 9, 6, 8, 4, 3, 7]
print(data)
unique = ()
for elem in data:
    if elem not in unique:
        unique += (elem,)
print(unique)

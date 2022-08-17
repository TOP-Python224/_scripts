a = range(5)
print(f"{a = }")
print(f"{type(a) = }")
print(f"{len(a) = }\n")
print(*a, end='\n\n')

print('range(10)')
print(*range(10), end='\n\n')

print('range(20)')
print(*range(20), end='\n\n')

print('range(10, 20)')
print(*range(10, 20), end='\n\n')

print('range(-10, 10)')
print(*range(-10, 10), end='\n\n')

print('range(10, -10)')
print(*range(10, -10), end='\n\n')

print('range(10, -10, -1)')
print(*range(10, -10, -1), end='\n\n')

print('range(10, 101, 10)')
print(*range(10, 101, 10), end='\n\n')


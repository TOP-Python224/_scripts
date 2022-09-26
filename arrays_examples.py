from array import array

small_numbers = array('b')
print(f'{small_numbers = }\n{type(small_numbers) = }\n')

while True:
    inp = input(' > ')
    if not inp:
        break
    
    small_numbers.append(int(inp))

print(small_numbers, end='\n\n')

small_numbers.append(128)

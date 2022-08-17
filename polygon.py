x1, y1 = 0, 0
perimeter = 0
while x2 := input('\nx координата > '):
    x2 = int(x2)
    y2 = int(input('y координата > '))
    
    perimeter += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    x1, y1 = x2, y2

perimeter += ((0 - x1)**2 + (0 - y1)**2)**0.5

print(f"{perimeter:.2f}")

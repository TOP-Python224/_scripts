mammals = {'тигр', 'верблюд', 'баран', 'кит', 'морж'}
aquatic = {'осьминог', 'кальмар', 'краб', 'кит', 'морж'}

aquatic_mammals = {'кит', 'морж'}
print(f'{aquatic_mammals.issubset(mammals) = }')
print(f'{aquatic_mammals < mammals = }\n')

print(f'{mammals.issuperset(aquatic_mammals) = }')
print(f'{mammals > aquatic_mammals = }\n')

print(f'{mammals.intersection(aquatic) = }')
print(f'{mammals & aquatic = }\n')

print(f'{mammals.union(aquatic) = }')
print(f'{mammals | aquatic = }\n')

print(f'{mammals.difference(aquatic) = }')
print(f'{mammals - aquatic = }\n')

print(f'{aquatic.difference(mammals) = }')
print(f'{aquatic - mammals = }\n')

print(f'{aquatic.symmetric_difference(mammals) = }')
print(f'{aquatic ^ mammals = }\n')

print(f'{aquatic.isdisjoint(mammals) = }')

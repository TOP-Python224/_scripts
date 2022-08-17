d1 = {'a': 12}
d2 = {'b': 23}

d2.update(d1)
print(f'{d2 = }\n')


d1 = {'a': 12, 'b': 41}
d2 = {'b': 23, 'c': 56}

d1.update(d2)
print(f'{d1 = }\n')

d1 = {'a': 12, 'b': 41}
d2 = {'b': 23, 'c': 56}

d2.update(d1)
print(f'{d2 = }\n')


d1 = {'a': 12, 'b': 41}
d2 = {'b': 23, 'c': 56}

d3 = d1 | d2
print(f'{d3 = }\n')

d4 = ({0.01: 'agg', 0.02: 'tag'}
      | {0.12: 'ttg'}
      | {0.41: 'cac'})
print(f'{d4 = }\n')

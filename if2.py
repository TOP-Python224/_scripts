obj = input('object literal: ')

if obj == 'a':
    print('str')
elif obj == '0':
    print('int')
elif obj == '[]':
    print('list')
elif obj == '()':
    print('tuple')
elif obj == '{}':
    print('dict')
else:
    print('unknown type')

def z():
    return d + e

a = 1
b = 2

try:
    print(z())
except ValueError:
    print('\n')
except NameError:
    pass
else:
    print('success')
finally:
    print('always')

# d = a + c
# e = b + c
# d = a + c
# print(d, e)
# e = b + c
# print(d, e)

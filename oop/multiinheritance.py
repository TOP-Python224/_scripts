from pprint import pprint


class A:
    class_attr1 = 10

class B:
    class_attr1 = 'xyz'
    class_attr2 = True


class C(A, B):
    pass

class D(B, A):
    pass


print(C.__mro__, end='\n\n')
pprint({
    attr: getattr(C, attr)
    for attr in dir(C)
    if not attr.startswith('__')
})
print('\n')

print(D.__mro__, end='\n\n')
pprint({
    attr: getattr(D, attr)
    for attr in dir(D)
    if not attr.startswith('__')
})

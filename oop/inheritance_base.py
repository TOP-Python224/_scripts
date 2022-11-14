from pprint import pprint


# родительский (базовый) класс (надкласс, superclass)
class A:
    class_attr = 'CONSTANT'

    def __init__(self):
        self.inst_attr = 10


# дочерний класс (подкласс, subclass)
class B(A):
    pass


# собственное пространство имён объекта класса
pprint(A.__dict__)

a = A()
# собственное пространство имён объекта экземпляра
print(a.__dict__)
print(a.class_attr, end='\n\n')


# собственное пространство имён объекта класса
pprint(B.__dict__)
# область видимости объекта класса
pprint(dir(B))

# B.__call__()
#     instance = object.__new__()
#     B.__init__(instance)
#         -> функция не найдена в собственном пространстве имён объекта класса
#         -> A.__init__(instance)
#     return instance
b = B()
# собственное пространство имён объекта экземпляра
print(b.__dict__, end='\n\n')


# цепочка наследования (method resolution order)
print(A.__mro__)
print(B.__mro__)

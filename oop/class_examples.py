class TestClass:
    # атрибуты класса
    # поля
    attr1 = 10
    attr2 = 'pq'

    # методы
    def __init__(self, param1: float = 0):
        """Специальный метод-конструктор."""
        self.inst_attr1 = [True, False]
        self.inst_attr2 = param1

    def func1(self):
        print('функция в классе TestClass')


# объект класса
print(TestClass)

# создание (instantiate) экземпляра (instance) класса
tc1 = TestClass()
# цепочка вызовов поэтапно
# TestClass(*args, **kwargs)
#     TestClass.__call__(*args, **kwargs):
#         obj = TestClass.__new__()
#         TestClass.__init__(obj, *args, **kwargs)
#         return obj
tc2 = TestClass(0.25)
print(tc1, end='\n\n')

print(TestClass.attr1)
print(TestClass.attr2, end='\n\n')

# атрибуты класса доступны для всех экземпляров данного класса
print(tc1.attr1 is tc2.attr1 is TestClass.attr1, end='\n\n')

print(TestClass.func1)
# вызов функции от объекта класса
TestClass.func1(None)
print()

print(tc1.func1)
# вызов метода от объекта экземпляра
tc1.func1()
# tc1.func1() -> TestClass.func1(tc1)
# экземпляр.метод() -> класс.функция(экземпляр)
print()

# создание нового атрибута для экземпляра
tc1.param_pam_pam = 'парам-пам-пам'
# изменение существующего атрибута
tc1.inst_attr1 = [False, False]

# вывод словаря, содержащего поля объекта
print(tc1.__dict__)
print(tc2.__dict__)

# вывод области видимости объекта
print([attr for attr in dir(tc1) if not attr.startswith('__')])

from pprint import pprint


class Proteus:
    @staticmethod
    def move():
        print('движение')

    @staticmethod
    def eat():
        print('питание')

    @staticmethod
    def reproduce():
        print('размножение')


class Fish(Proteus):
    @staticmethod
    def breath():
        print('дыхание')


class Reptile(Fish):
    @staticmethod
    def hide():
        print('скрытность')


class Bird(Reptile):
    @staticmethod
    def fly():
        print('полёт')


class Mammals(Reptile):
    @staticmethod
    def care():
        print('забота')


class Human(Mammals):
    @staticmethod
    def speak():
        print('привет!')


pprint(Human.__mro__)
print()

vasya = Human()
# атрибуты экземпляра, не считая встроенных
print([attr for attr in dir(vasya) if not attr.startswith('__')])

quesha = Bird()
# атрибуты экземпляра, не считая встроенных
print([attr for attr in dir(quesha) if not attr.startswith('__')])

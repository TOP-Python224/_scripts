"""Демонстратор адаптера для нескольких классов."""


class Dog:
    @staticmethod
    def bark():
        print('гав')


class Cat:
    @staticmethod
    def meow():
        print('мяу')


class Person:
    @staticmethod
    def hello():
        print('привет')


class Car:
    @staticmethod
    def move(speed: int = 60):
        print('вр' + 'у'*(speed//20) + 'м')


class Adapted:
    def __init__(self, obj_to_adapt, **methods):
        self.obj = obj_to_adapt
        self.__dict__ |= methods

    def __getattr__(self, attribute_name: str):
        return getattr(self.obj, attribute_name)


# объекты для адаптации
zhuchka = Dog()
barsik = Cat()
egor = Person()
uaz = Car()

# адаптированные объекты
objects = [
    Adapted(zhuchka, make_noise=zhuchka.bark),
    Adapted(barsik, make_noise=barsik.meow),
    Adapted(egor, make_noise=egor.hello),
    Adapted(uaz, make_noise=uaz.move),
]

for obj in objects:
    obj.make_noise()

print()

objects[0].bark()
objects[-1].make_noise(100)

class Car:
    # полиморфный метод
    @staticmethod
    def move():
        print('машина едет')

    # без полиморфизма
    # @staticmethod
    # def drive():
    #     print('машина едет')


class Person:
    # полиморфный метод
    @staticmethod
    def move():
        print('человек идёт')

    # без полиморфизма
    # @staticmethod
    # def walk():
    #     print('человек идёт')


car = Car()
human = Person()

for obj in (car, human):
    # использование полиморфного метода
    obj.move()

    # без полиморфизма
    # if isinstance(obj, Car):
    #     obj.drive()
    # elif isinstance(obj, Person):
    #     obj.walk()


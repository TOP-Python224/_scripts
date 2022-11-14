class Vehicle:
    wheels = 4

    @staticmethod
    def move():
        print('двигается горизонтально по твёрдой поверхности в любом направлении')


class Car(Vehicle):
    pass


class Bycycle(Vehicle):
    wheels = 2


class Train(Vehicle):
    wheels = 12

    @staticmethod
    def move():
        print('двигается по рельсам')


class Helicopter(Vehicle):
    wheels = 0

    @staticmethod
    def move():
        print('передвигается по воздуху в любом направлении')


vehicles = (
    Bycycle(),
    Car(),
    Train(),
    Helicopter()
)
for v in vehicles:
    print(f'У {v.__class__.__name__.lower()} {v.wheels} колёс и он', end=' ')
    v.move()

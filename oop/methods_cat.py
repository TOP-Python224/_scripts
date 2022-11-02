from random import choice, randrange as rr


class Cat:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def hunt():
        return choice(('охота прошла успешно', 'охота прошла неудачно'))

    @classmethod
    def birth(cls):
        return tuple(cls('') for _ in range(rr(2, 6)))


yara = Cat('Яра')

print(Cat.hunt)
print(yara.hunt)

hunt_result1 = Cat.hunt()
hunt_result2 = yara.hunt()
# yara.hunt() -> Cat.hunt()
print(hunt_result1, hunt_result2, end='\n\n')

print(Cat.birth)
print(yara.birth)

kittens1 = Cat.birth()
# Cat.birth() -> Cat.__class__.birth(Cat)
kittens2 = yara.birth()
# yara.birth() -> yara.__class__.__class__.birth(yara.__class__)
print(kittens1, kittens2, end='\n\n')

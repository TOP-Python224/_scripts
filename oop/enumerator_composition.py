from enum import Enum


class Person:

    class Gender(Enum):
        M = 'male'
        F = 'female'

    def __init__(self, name: str, gender: 'Person.Gender'):
        self.name: str = name
        self.gender: Person.Gender = gender

    def __str__(self):
        return f'{self.name} ({self.gender.value})'


print(repr(Person.Gender.M))
print(type(Person.Gender.M))
print(repr(Person.Gender.M.name))
print(repr(Person.Gender.M.value), end='\n\n')

anatoliy = Person('Anatoliy', Person.Gender.M)
print(anatoliy)


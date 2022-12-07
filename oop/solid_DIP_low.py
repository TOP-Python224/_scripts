"""Dependencies Inversion Principle — Принцип Инверсии Зависимостей"""

from enum import Enum
from dataclasses import dataclass


class Relation(Enum):
    PARENT = 0
    CHILD = 1


@dataclass
class Person:
    name: str

    def __str__(self):
        return self.name


class Relationship:
    def __init__(self):
        self.db: list = []

    def add_relation(self, parent: Person, child: Person):
        self.db += [
            (parent, Relation.PARENT, child),
            (child, Relation.CHILD, parent),
        ]

    def find_all_children(self, parent_name: str):
        for pers1, relation, pers2 in self.db:
            if pers1.name.lower() == parent_name.lower():
                if relation is Relation.PARENT:
                    yield pers2


john = Person('John')
kate = Person('Kate')
adam = Person('Adam')
lucy = Person('Lucy')
paul = Person('Paul')
elen = Person('Elen')

storage = Relationship()
storage.add_relation(john, adam)
storage.add_relation(john, lucy)
storage.add_relation(kate, adam)
storage.add_relation(kate, lucy)
storage.add_relation(paul, elen)

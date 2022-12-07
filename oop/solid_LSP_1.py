"""Liskov Substitution Principle — Принцип Подстановки Лисков"""

from random import choice
from string import ascii_lowercase


parent_class = int
child_class = bool
print(bool.__mro__)


def high_level_code(obj: parent_class | child_class):
    return list(ascii_lowercase)[obj]


parent_class_object = choice([3, 5, 8])
child_class_object = choice([True, False])

print(high_level_code(parent_class_object))
print(high_level_code(child_class_object))

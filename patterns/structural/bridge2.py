"""Демонстратор моста 2."""

from abc import ABC, abstractmethod


class Material(ABC):
    hits: float
    @abstractmethod
    def __str__(self):
        pass

class Straw(Material):
    hits = 0.75
    def __str__(self):
        return 'straw'

class Wood(Material):
    hits = 1
    def __str__(self):
        return 'wood'

class Cobblestone(Material):
    hits = 1.5
    def __str__(self):
        return 'cobblestone'

class Brick(Material):
    hits = 1.25
    def __str__(self):
        return 'brick'


class Building(ABC):
    base_hitpoints: int

    def __init__(self, material: Material):
        self.material = material
        self.hitpoints = int(self.base_hitpoints * material.hits)

    @abstractmethod
    def __str__(self):
        pass


class Watchtower(Building):
    base_hitpoints = 300

    def __init__(self, material: Material, name: str):
        super().__init__(material)
        self.name = name

    def __str__(self):
        return f'{self.material} watchtower {self.name}: {self.hitpoints} HP'


class Mill(Building):
    base_hitpoints = 150

    def __init__(self, material: Material, name: str):
        super().__init__(material)
        self.name = name

    def __str__(self):
        return f'{self.material} mill {self.name}: {self.hitpoints} HP'


west_tower = Watchtower(
    Cobblestone(),
    'of the west border'
)
print(west_tower)

hill_mill = Mill(
    Brick(),
    'on the green hill'
)
print(hill_mill)

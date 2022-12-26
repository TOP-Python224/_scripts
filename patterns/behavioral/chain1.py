from dataclasses import dataclass
from typing import Optional


@dataclass
class Creature:
    name: str
    attack: int
    defense: int

    def __str__(self):
        return f"{self.name}: {self.attack}/{self.defense}"


class CreatureModifier:
    """Базовый класс модификаторов, являющийся корневым элементом цепочки модификаторов и предоставляющий методы для прохождения по всем элементам цепочки."""
    def __init__(self, creature: Creature):
        self.creature = creature
        self.prev_modifier: Optional[CreatureModifier] = None
        self.next_modifier: Optional[CreatureModifier] = None

    def add_modifier(self, modifier: 'CreatureModifier'):
        if self.next_modifier is None:
            self.next_modifier = modifier
            modifier.prev_modifier = self
        else:
            self.next_modifier.add_modifier(modifier)

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.defense <= self.creature.attack:
            self.creature.defense += 1
        super().handle()


goblin = Creature('Гоблин', 1, 1)
print(goblin)

inventory = CreatureModifier(goblin)

inventory.add_modifier(DoubleAttackModifier(goblin))
inventory.add_modifier(IncreaseDefenseModifier(goblin))

inventory.handle()

print(goblin)

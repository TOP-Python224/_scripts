from abc import ABC, abstractmethod
from random import randrange

from countable_nouns import countable_nouns


class BaseCreature(ABC):
    """Все игровые существа наследуют атрибуты, определённые в этом классе."""
    @abstractmethod
    def die(self):
        """Все существа могут умереть — вопрос только как именно."""


class Enemy(BaseCreature):
    """Игровые противники (мобы)."""
    def __init__(self, hp: int):
        self.hp = hp
        self.drop = randrange(3, 20)

    def die(self):
        """При смерти из мобов выпадают монеты."""
        word = countable_nouns(self.drop, ('монета', 'монеты', 'монет'))
        print(f"Выпало: {self.drop} {word}")


class Trader(BaseCreature):
    """Персонажи, обслуживающие игровую экономику."""
    def die(self):
        """Убийство торговцев должно быть наказуемо."""
        print('За вами выехали')


mob1 = Enemy(100)
print(mob1)
mob1.die()

tr1 = Trader()
tr1.die()

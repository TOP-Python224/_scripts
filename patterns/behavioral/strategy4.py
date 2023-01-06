from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import Optional


class Item(Enum):
    ROCK = 'камень'
    SCISSORS = 'ножницы'
    PAPER = 'бумага'

    @classmethod
    def random(cls) -> 'Item':
        return choice(list(cls))


class Tie(Exception):
    pass


class Strategy(ABC):
    """Абстрактный класс для стратегий игры КНБ."""
    item: Item

    @staticmethod
    @abstractmethod
    def check(strategy: 'Strategy') -> bool:
        """Возвращает результат столкновения текущей стратегии с остальными."""

    def __str__(self):
        return self.item.value


class Rock(Strategy):
    item = Item.ROCK

    @staticmethod
    def check(strategy: Strategy) -> bool:
        if strategy.item is Item.SCISSORS:
            return True
        elif strategy.item is Item.PAPER:
            return False
        elif strategy.item is Item.ROCK:
            raise Tie


class Scissors(Strategy):
    item = Item.SCISSORS

    @staticmethod
    def check(strategy: Strategy) -> bool:
        if strategy.item is Item.PAPER:
            return True
        elif strategy.item is Item.ROCK:
            return False
        elif strategy.item is Item.SCISSORS:
            raise Tie


class Paper(Strategy):
    item = Item.PAPER

    @staticmethod
    def check(strategy: Strategy) -> bool:
        if strategy.item is Item.ROCK:
            return True
        elif strategy.item is Item.SCISSORS:
            return False
        elif strategy.item is Item.PAPER:
            raise Tie


class Random(Strategy):
    item = Item.random()

    def check(self, strategy: Strategy) -> bool:
        if self.item is Item.ROCK:
            return Rock.check(strategy)
        elif self.item is Item.PAPER:
            return Paper.check(strategy)
        elif self.item is Item.SCISSORS:
            return Scissors.check(strategy)


items_to_strategies = {
    Item.ROCK: Rock,
    Item.SCISSORS: Scissors,
    Item.PAPER: Paper,
}


class Player:
    """Объект с различными стратегиями игры."""
    def __init__(self, name: str, strategy_name: Optional[Item] = None):
        self.name = name
        self.change_strategy(strategy_name)

    def change_strategy(self, strategy_name: Optional[Item] = None):
        if strategy_name is None:
            self.strategy = Random()
        elif isinstance(strategy_name, Item):
            self.strategy = items_to_strategies[strategy_name]()
        else:
            raise

    def play(player1, player2: 'Player'):
        """Метод-интерфейс для одного раунда."""
        if VERBOSE:
            print(f'{player1.name}: {player1.strategy}')
            print(f'{player2.name}: {player2.strategy}')
        try:
            result = player1.strategy.check(player2.strategy)
            if result:
                print(f'{player1.name} победил')
            else:
                print(f'{player2.name} победил')
        except Tie:
            print(f'Ничья')

    def __str__(self):
        return self.name


VERBOSE = True

pl1 = Player('Игнат', Item.ROCK)
pl2 = Player('Тимофей')

pl1.play(pl2)

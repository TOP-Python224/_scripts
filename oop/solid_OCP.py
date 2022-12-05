"""Opened/Closed Principle — Принцип Открытости/Закрытости"""

from enum import Enum
from dataclasses import dataclass
from collections.abc import Iterable
from abc import ABC, abstractmethod


class Color(Enum):
    BLACK = '#000'
    RED = '#f00'
    GREEN = '#0f0'
    BLUE = '#00f'
    WHITE = '#fff'

    # def match(self, item: 'Product') -> bool:
    #     return item.color is self

class Size(Enum):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    # def match(self, item: 'Product') -> bool:
    #     return item.size is self


@dataclass
class Product:
    name: str
    color: Color
    size: Size

    def __str__(self):
        return f'{self.name} {self.color.name} {self.size.name}'


# является нарушением OCP
# количество методов зависит от количества критериев по которым осуществляется фильтрация
#   a b -> a b a&b a|b
#   a b c -> a b c a&b b&c a&c a|b b|c a|c a&b&c a|b|c
#   a b c d -> a b c d a&b b&c c&d a&c b&d a&d a|b b|c c|d a|c b|d a|d a&b&c a|b|c a&b&d a|b|d ...
# экспоненциальный рост количества методов
@dataclass
class Filter:
    products: Iterable[Product]

    def by_color(self, color: Color):
        for pr in self.products:
            if pr.color is color:
                yield pr

    def by_size(self, size: Size):
        for pr in self.products:
            if pr.size is size:
                yield pr

    def by_color_and_size(self, color: Color, size: Size):
        for pr in self.products:
            if pr.color is color and pr.size is size:
                yield pr

    def by_color_or_size(self, color: Color, size: Size):
        for pr in self.products:
            if pr.color is color or pr.size is size:
                yield pr


# масштабируемая модель
class Criteria(ABC):
    @abstractmethod
    def match(self, item: Product) -> bool:
        """Проверяет на соответствие определённый параметр переданного продукта."""


@dataclass
class ColorCriteria(Criteria):
    color: Color

    def match(self, item: Product) -> bool:
        return item.color is self.color


@dataclass
class SizeCriteria(Criteria):
    size: Size

    def match(self, item: Product) -> bool:
        return item.size is self.size


class AndCriteria(Criteria):
    def __init__(self, *criterias: Criteria):
        self.criterias = criterias

    def match(self, item: Product) -> bool:
        return all(map(
            lambda crit: crit.match(item),
            self.criterias
        ))


class OrCriteria(Criteria):
    def __init__(self, *criterias: Criteria):
        self.criterias = criterias

    def match(self, item: Product) -> bool:
        return any(map(
            lambda crit: crit.match(item),
            self.criterias
        ))


@dataclass
class BetterFilter:
    products: Iterable[Product]

    def filter(self, criteria: Criteria):
        for product in self.products:
            if criteria.match(product):
                yield product


goods = [
    Product('Гранат', Color.RED, Size.MEDIUM),
    Product('Арбуз', Color.GREEN, Size.LARGE),
    Product('Виноград', Color.GREEN, Size.SMALL),
    Product('Слива', Color.BLUE, Size.SMALL),
    Product('Хурма', Color.RED, Size.SMALL),
]


# тестирование класса-нарушителя
# simple_filter = Filter(goods)

# red_fruits = simple_filter.by_color(Color.RED)
# print(*red_fruits, sep='\n', end='\n\n')

# small_fruits = simple_filter.by_size(Size.SMALL)
# print(*small_fruits, sep='\n', end='\n\n')

# green_and_large_fruits = simple_filter.by_color_and_size(Color.GREEN, Size.LARGE)
# print(*green_and_large_fruits, sep='\n', end='\n\n')

# blue_or_medium_fruits = simple_filter.by_color_or_size(Color.BLUE, Size.MEDIUM)
# print(*blue_or_medium_fruits, sep='\n', end='\n\n')


# тестирование масштабируемой модели
red = ColorCriteria(Color.RED)
green = ColorCriteria(Color.GREEN)
blue = ColorCriteria(Color.BLUE)
small = SizeCriteria(Size.SMALL)
medium = SizeCriteria(Size.MEDIUM)
large = SizeCriteria(Size.LARGE)
green_and_large = AndCriteria(green, large)
blue_or_medium = OrCriteria(blue, medium)
red_or_blue = OrCriteria(red, blue)

better_filter = BetterFilter(goods)

red_fruits = better_filter.filter(red)
print(*red_fruits, sep='\n', end='\n\n')

small_fruits = better_filter.filter(small)
print(*small_fruits, sep='\n', end='\n\n')

green_and_large_fruits = better_filter.filter(green_and_large)
print(*green_and_large_fruits, sep='\n', end='\n\n')

blue_or_medium_fruits = better_filter.filter(blue_or_medium)
print(*blue_or_medium_fruits, sep='\n', end='\n\n')

red_or_blue_fruits = better_filter.filter(red_or_blue)
print(*red_or_blue_fruits, sep='\n', end='\n\n')

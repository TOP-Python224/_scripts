from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass


class VectorObject(ABC):
    @abstractmethod
    def render(self):
        pass


@dataclass
class Line(VectorObject):
    name: str

    def render(self):
        print(self.name)


@dataclass
class Text(VectorObject):
    name: str
    text: str

    def render(self):
        print(self.text)


class GroupObject(VectorObject):
    def __init__(self, name: str):
        self.name = name
        self.__elements: list[VectorObject] = []

    @property
    def elements(self):
        return iter(self.__elements)

    @elements.setter
    def elements(self, value: VectorObject | Sequence[VectorObject]):
        if isinstance(value, Sequence):
            self.__elements += list(value)
        elif isinstance(value, VectorObject):
            self.__elements += [value]
        else:
            raise TypeError


ab = Line('AB')
bc = Line('BC')
cd = Line('CD')
da = Line('DA')
formula = Text('perimeter_formula', 'P = AB + BC + CD + DA')

group = GroupObject('rectangle')
group.elements = ab
# выглядит как переопределение
group.elements = bc



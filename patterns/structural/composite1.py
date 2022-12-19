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

    def add_element(self, *objects: VectorObject):
        self.__elements += list(objects)

    def render(self):
        for obj in self.__elements:
            obj.render()


ab = Line('AB')
bc = Line('BC')
cd = Line('CD')
da = Line('DA')
formula = Text('perimeter_formula', 'P = AB + BC + CD + DA')

ab.render()
formula.render()

print()


group = GroupObject('rectangle')

figure = (ab, bc, formula, cd, da)
group.add_element(*figure)

group.render()

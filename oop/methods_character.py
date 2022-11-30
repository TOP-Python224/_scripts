from itertools import count
from datetime import datetime as dt

levels = [q*i for q, i in zip(range(10, 100), count(1))]
classes = ['богатырь', 'волхв', 'сапожник']


class Character:
    """
    Описывает игрового персонажа с набором характеристик и действий.
    """
    __saves: dict['Character', dt] = {}

    def __init__(self, name: str, class_name: str):
        self.name = name.title()
        self.experience: int = 0
        self.class_ = class_name if self.valid_class_name(class_name) else None

    @property
    def level(self):
        for limit in levels:
            lvl = self.experience // limit
            if lvl:
                return lvl+1

    def save(self) -> None:
        self.__class__.__saves |= {
            (self.name, self.experience, self.class_): dt.now()
        }

    @classmethod
    def load(cls) -> 'Character':
        for i, character in enumerate(cls.__saves, 1):
            name, exp, class_ = character
            print(f'{i}. {name}: {exp} — {cls.__saves[character]}')
        i = int(input(' > введите номер сохранения: '))
        name, exp, class_ = list(cls.__saves)[i-1]
        character = Character(name, class_)
        character.experience = exp
        return character

    def __str__(self):
        return f'<{self.name}: lvl={self.level}>'

    @staticmethod
    def valid_class_name(class_name: str) -> bool:
        return class_name.lower() in classes


pers = Character('Илья-муромец', 'богатырь')
pers.experience = 23
pers.save()

del pers

loaded_pers = Character.load()
print(loaded_pers)

loaded_pers.experience += 100
loaded_pers.save()

print(loaded_pers.load())


print(Character.valid_class_name('чародей'))

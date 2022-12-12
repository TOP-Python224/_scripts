"""Шаблон Строитель"""

from pathlib import Path
from sys import path


class HTMLTag:
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = ''):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []

    @property
    def nested(self):
        return iter(self.__nested)

    @nested.setter
    def nested(self, value: 'HTMLTag'):
        self.__nested += [value]

    def __str(self, indent_level: int) -> str:
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result

    def __str__(self):
        return self.__str(0)

    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = ''):
        return HTMLBuilder(name, value)


class HTMLBuilder:
    def __init__(self, root: HTMLTag | str, value: str = ''):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')

    def nested(self, name: str, value: str = ''):
        tag = HTMLTag(name, value)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = ''):
        tag = HTMLTag(name, value)
        self.root.nested = tag
        return self

    def build(self):
        return self.root


root = HTMLTag.create('div')
root.sibling('p', 'Menu')\
    .nested('ul')\
    .sibling('li', 'File')\
    .sibling('li', 'Edit')\
    .sibling('li', 'View')
div = root.build()
print(div)

script_dir = Path(path[0])
(script_dir / 'example.html').write_text(str(div), encoding='utf-8')

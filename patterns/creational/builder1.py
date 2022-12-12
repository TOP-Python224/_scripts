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


ul = HTMLTag('ul')
ul.nested = HTMLTag('li', 'File')
ul.nested = HTMLTag('li', 'Edit')
ul.nested = HTMLTag('li', 'View')

div = HTMLTag('div')
div.nested = HTMLTag('p', 'Menu')
div.nested = ul

script_dir = Path(path[0])
(script_dir/'example.html').write_text(str(div), encoding='utf-8')

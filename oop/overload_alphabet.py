from typing import Literal


class Alphabet:
    """Генерирует последовательность символов алфавита заданного языка в заданном регистре (нижний по умолчанию).

    Экземпляр класса ведёт себя как неизменяемая индексируемая последовательность, индексация начинается с 1.

    Генерация символов производится с помощью кодировочной страницы UTF-8 (65001).
    """
    def __init__(self,
                 lang_code: Literal['ru', 'en', 'jp'],
                 uppercase: bool = False):
        self.code = lang_code
        self.__chars: tuple[str, ...] = ()
        self.__generate_chars(uppercase)

    def __generate_chars(self, uppercase: bool):
        if self.code == 'ru':
            start_code = (1072, 1040)[uppercase]
            self.__chars = tuple(chr(code) for code in range(start_code, start_code + 6)) \
                           + tuple(chr((1105, 1025)[uppercase])) \
                           + tuple(chr(code) for code in range(start_code+6, start_code+32))

        elif self.code == 'en':
            start_code = (97, 65)[uppercase]
            self.__chars = tuple(chr(code) for code in range(start_code, start_code + 26))

        elif self.code == 'jp':
            self.__chars = ('あ', 'い', 'う', 'え', 'お',
                            'た', 'ち', 'つ', 'て', 'と',
                            'さ', 'し', 'す', 'せ', 'そ',
                            'か', 'き', 'く', 'け', 'こ',
                            'な', 'に', 'ぬ', 'ね', 'の',
                            'は', 'ひ', 'ふ', 'ヘ', 'ほ',
                            'ま', 'み', 'む', 'め', 'も',
                            'よ', 'ゆ', 'や',
                            'ら', 'り', 'る', 'れ', 'ろ',
                            'わ', 'を', 'ん')

    def __len__(self):
        return len(self.__chars)

    def __contains__(self, item: str):
        if isinstance(item, str):
            return item in self.__chars
        else:
            raise TypeError

    def __iter__(self):
        return iter(self.__chars)

    def __getitem__(self, index: int):
        if isinstance(index, int):
            if 0 < index <= len(self.__chars):
                return self.__chars[index - 1]
            else:
                raise IndexError
        else:
            raise TypeError

    # методы __setitem__() и __delitem__() не определены для исключения возможности изменять элементы объекта

    def __repr__(self):
        q = ', '.join(self.__chars[:5])
        return f'<{self.code.upper()}: ({q[:-1]}...)>'

    def __str__(self):
        return ' '.join(self.__chars)


eng = Alphabet('en')
rus = Alphabet('ru', True)
jap = Alphabet('jp')

print(len(jap))
print('Ё' in rus)

for char in eng:
    print(char, end=' ')
print()

print(rus[1], rus[7], rus[33])

print(repr(jap))
print(rus)

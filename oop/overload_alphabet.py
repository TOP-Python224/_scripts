from typing import Literal


class Alphabet:
    def __init__(self,
                 lang_code: Literal['ru', 'en', 'jp'],
                 uppercase: bool = False):
        self.code = lang_code
        self.chars: list[str] = []
        self.__generate_chars(uppercase)

    def __generate_chars(self, uppercase: bool):
        if self.code == 'ru':
            start_code = (1072, 1040)[uppercase]
            self.chars = [chr(code) for code in range(start_code, start_code+6)]\
                         + [chr((1105, 1025)[uppercase])]\
                         + [chr(code) for code in range(start_code+6, start_code+32)]

        elif self.code == 'en':
            start_code = (97, 65)[uppercase]
            self.chars = [chr(code) for code in range(start_code, start_code+26)]

        elif self.code == 'jp':
            self.chars = ['あ', 'い', 'う', 'え', 'お',
                          'た', 'ち', 'つ', 'て', 'と',
                          'か', 'き', 'く', 'け', 'こ',
                          'さ', 'し', 'す', 'せ', 'そ',
                          'ま', 'み', 'む', 'め', 'も',
                          'な', 'に', 'ぬ', 'ね', 'の',
                          'は', 'ひ', 'ふ', 'ヘ', 'ほ',
                          'ら', 'り', 'る', 'れ', 'ろ',
                          'よ', 'ゆ', 'や', 'ん', 'わ', 'を']


eng = Alphabet('en')

print()

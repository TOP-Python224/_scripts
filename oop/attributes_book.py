from datetime import datetime as dt


class Book:
    """Описывает литературное произведение."""
    def __init__(self,
                 title: str,
                 authors: list[str],
                 genre: str,
                 date_of_writing: str,
                 language: str,
                 symbols: int) -> None:
        """
        :param title: наименование произведения
        :param authors: список из одной и более строк, содержащих фамилию и имя авторов
        :param genre: название жанра
        :param date_of_writing: дата написания произведения в формате дд.мм.гггг
        :param language: язык оригинала
        :param symbols: количество знаков (без пробельных)
        """
        self.title = title
        if len(authors) > 0:
            self.authors = authors
        else:
            raise ValueError('у произведения должен быть хотя бы один автор')
        self.genre = genre
        self.date = dt.strptime(date_of_writing, '%d.%m.%Y').date()
        self.language = language
        self.symbols = symbols

    def __repr__(self) -> str:
        return f'<Book: {self.title}>'

    def __str__(self) -> str:
        authors = ', '.join(a.split()[0] for a in self.authors)
        return '. '.join((authors, self.title))


books = [
    Book("Дети времени", ["Чайковски Адриан"], "фантастика", "18.12.2018", "английский", 500000),
    Book("Завтра вновь и вновь", ["Светерлич Том"], "мистика", "01.05.2010", "английский", 280000),
    Book("Севильский цирюльник", ["Бомарше Пьер"], "трагикомедия", "05.04.1773", "французский", 200000),
    Book("Благие знамения", ["Гейман Нил", "Пратчетт Терри"], "мистика", "20.10.2011", "английский", 450000),
]

for book in books:
    print(book)
print()

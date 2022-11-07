import re


class Address:
    """Описывает адрес на территории РФ."""
    def __init__(self,
                 zipcode: str,
                 country: str,
                 region: str,
                 city: str,
                 street: str,
                 building_number: int,
                 building_liter: str,
                 entrance: int,
                 floor: int,
                 office: str):
        # запись в свойство — работает сеттер
        self.zipcode = zipcode
        self.country = country
        self.region = region
        self.city = city
        self.street = street
        # запись в свойство — работает сеттер
        self.number = building_number
        # запись в свойство — работает сеттер
        self.liter = building_liter
        # запись в свойство — работает сеттер
        self.entrance = entrance
        # запись в свойство — работает сеттер
        self.floor = floor
        self.office = office

    # геттер (getter) для получения значения атрибута
    @property
    def zipcode(self) -> str:
        return self._zipcode

    # сеттер (setter) для установки значения атрибута
    @zipcode.setter
    def zipcode(self, value: str) -> None:
        if re.fullmatch(r'\d{6}', value):
            self._zipcode = value
        else:
            raise ValueError('российский почтовый индекс состоит из шести цифр')

    @property
    def number(self) -> str:
        return str(self._number)

    @number.setter
    def number(self, value: int) -> None:
        if value > 0:
            self._number = value
        else:
            raise ValueError('номер дома может быть только натуральным числом')

    @property
    def liter(self) -> str:
        return self._liter

    @liter.setter
    def liter(self, value: str) -> None:
        value = value.lower()
        if re.fullmatch(r'[а-я]?', value):
            self._liter = value
        else:
            raise ValueError("российская почтовая литера дома представляет из себя одну букву от 'А' до 'Я'")

    @property
    def entrance(self) -> str:
        return str(self.__entrance)

    @entrance.setter
    def entrance(self, value: int) -> None:
        if value > 0:
            self.__entrance = value
        else:
            raise ValueError('номер подъезда может быть только натуральным числом')

    @property
    def floor(self) -> str:
        return self.__floor

    @floor.setter
    def floor(self, value: int) -> None:
        self.__floor = str(value)

    def __str__(self):
        return f'{self.zipcode}, {self.country}, {self.region}, {self.city}, {self.street} {self.number}{self.liter} – {self.office}'



ekb_TOP = Address('620026', 'Россия', 'Свердловская область', 'Екатеринбург', 'ул. Энгельса', 36, '', 2, 4, '419/2')
print(ekb_TOP)

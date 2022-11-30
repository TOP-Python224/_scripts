from dataclasses import dataclass


@dataclass
class Person:
    surname: str
    name: str
    patronymic: str

    @property
    def fio(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'

    @fio.setter
    def fio(self, full_name: str) -> None:
        surname, name, patronymic = full_name.split()
        self.surname = surname
        self.name = name
        self.patronymic = patronymic


teacher = Person('Фомин', 'Илья', 'Иванович')
print(teacher.fio)

teacher.fio = 'Шаповаленко Геннадий Дмитриевич'
print(teacher.surname)
print(teacher.name)
print(teacher.patronymic)

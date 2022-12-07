"""Interface Segregation Principle — Принцип Разделения Интерфейсов"""
import re
from abc import ABC, abstractmethod
from collections.abc import Callable


# нарушение ISP
class MultiFunctionDevice(ABC):
    """Абстрактный базовый класс (интерфейс) для устройств печати, сканирования и работы с факсами."""
    @staticmethod
    @abstractmethod
    def print(document):
        pass

    @staticmethod
    @abstractmethod
    def scan(document):
        pass

    @staticmethod
    @abstractmethod
    def fax(document):
        pass


class HPDeskJet(MultiFunctionDevice):
    """МФУ."""
    @staticmethod
    def print(document):
        print(document)

    @staticmethod
    def scan(document):
        document = input()
        return bool(document)

    @staticmethod
    def fax(document):
        print(f'fax: {document}')


class BrotherHL(MultiFunctionDevice):
    """Лазерный принтер."""
    @staticmethod
    def print(document):
        print(document)

    @staticmethod
    def scan(document):
        """метод не поддерживается"""
        raise NotImplementedError

    @staticmethod
    def fax(document):
        """метод не поддерживается"""
        raise NotImplementedError



hl5250dn = BrotherHL()

hl5250dn_methods = [
    attr
    for attr in dir(hl5250dn)
    if not re.fullmatch(r'__.*__', attr)
    if isinstance(getattr(hl5250dn, attr).__class__, Callable)
]
print(hl5250dn_methods)


# корректная по ISP реализация
class Printer(ABC):
    """Абстрактный базовый класс (интерфейс) для устройств печати."""
    @staticmethod
    @abstractmethod
    def print(document):
        pass

class Scanner(ABC):
    """Абстрактный базовый класс (интерфейс) для устройств сканирования."""
    @staticmethod
    @abstractmethod
    def scan(document):
        pass

class Fax(ABC):
    """Абстрактный базовый класс (интерфейс) для факсимильные устройств."""
    @staticmethod
    @abstractmethod
    def fax(document):
        pass


class BrotherHL(Printer):
    """Лазерный принтер."""
    @staticmethod
    def print(document):
        print(document)


class XeroxWorkCenter(Printer, Scanner, Fax):
    """МФУ."""
    @staticmethod
    def print(document):
        print(document)

    @staticmethod
    def scan(document):
        document = input()
        return bool(document)

    @staticmethod
    def fax(document):
        print(f'fax: {document}')



# импорт из стандартной библиотеки
from abc import ABC, abstractmethod
from enum import Enum

# импорт дополнительных пакетов и модулей текущего проекта
from . import logger


class Operation(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccount:
    """Адресат"""
    overdraft_limit: int = -500

    def __init__(self, initial_amount: int = 0):
        self.balance: int = initial_amount

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> bool:
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.balance}'

    def __str__(self):
        return f'денег на счёте: {self.balance}₽'


class Command(ABC):
    """Абстрактный класс команды."""
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class BAGeneral(Command):
    """Команда для базовых операций с банковским счётом."""
    def __init__(self,
                 bank_account: BankAccount,
                 operation: Operation,
                 amount: int):
        self.account = bank_account
        self.operation = operation
        self.amount = amount
        self.success: bool = False

    def __log(self, *, undo: bool = False) -> None:
        if undo:
            data = 'UNDO'
        else:
            data = 'OK' if self.success else 'FAIL'
        data += f' — {self.operation}: {self.amount}₽ — {self.account!r}₽'
        logger.Logger.append_log(data)

    def execute(self) -> None:
        if not self.success:
            if self.operation is Operation.DEPOSIT:
                self.account.deposit(self.amount)
                self.success = True
            elif self.operation is Operation.WITHDRAW:
                self.success = self.account.withdraw(self.amount)
            self.__log()

    def undo(self):
        if self.success:
            if self.operation is Operation.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.operation is Operation.WITHDRAW:
                self.account.deposit(self.amount)
            self.__log(undo=True)
            self.success = False


class BATransfer(Command):
    """Команда для перевода средств с одного банковского счёта на другой."""
    def __init__(self,
                 from_bank_account: BankAccount,
                 to_bank_account: BankAccount,
                 amount: int):
        self._from = from_bank_account
        self._to = to_bank_account
        self.amount = amount
        self.success: bool = False

    def execute(self) -> None:
        wd = BAGeneral(self._from, Operation.WITHDRAW, self.amount)
        wd.execute()
        if wd.success:
            BAGeneral(self._to, Operation.DEPOSIT, self.amount).execute()
            self.success = True

    def undo(self) -> None:
        if self.success:
            wd = BAGeneral(self._to, Operation.WITHDRAW, self.amount)
            wd.execute()
            if wd.success:
                BAGeneral(self._from, Operation.DEPOSIT, self.amount).execute()
                self.success = False


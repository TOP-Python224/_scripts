from datetime import datetime as dt


class Organization:
    def __init__(self, name: str, inn: str):
        self.name = name
        self.inn = inn
        self._budget = 0
        self.__budget_calendar = {}

    def __set_budget(self, amount: int):
        if dt.now().year not in self._budget:
            self.__budget_calendar[dt.now().year] = amount
            self._budget = amount


org = Organization('Рога-и-Копыта', '123456789')
print(org.__dict__)


org.budget = 100000
org.budget = 'денег-нет-шлите-телеграммы'

print(org.__dict__)


org._budget = 233500
print(org._budget)
print(org.__dict__)


print(org._Organization__budget_calendar)
org._Organization__budget_calendar = (1, 2, 3)
print(org.__dict__)


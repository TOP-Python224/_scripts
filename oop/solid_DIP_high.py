"""Dependencies Inversion Principle — Принцип Инверсии Зависимостей"""

import solid_DIP_low as rel_db


class Research:
    def __init__(self):
        self.db = rel_db.storage

    # нарушение DIP
    # def find_all_children(self, parent_name: str):
    #     # зависимость от реализации кода нижнего уровня
    #     for pers1, relation, pers2 in self.db:
    #         if pers1.name.lower() == parent_name.lower():
    #             if relation is rel_db.Relation.PARENT:
    #                 yield pers2

    def find_all_children(self, parent_name: str):
        return self.find_all_children(parent_name)


r = Research()
print(*r.find_all_children('john'))

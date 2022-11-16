from datetime import datetime as dt


class Recipe(dict):
    def __init__(self, name: str, portions: int, prepare_time: str, **ingredients):
        """
        :param name: название блюда
        :param portions: количество порций
        :param prepare_time: время приготовления блюда в формате ч:мм
        :param ingredients: каждому ингредиенту сопоставляется строка с указанием количества этого ингредиента
        """
        super().__init__(**ingredients)
        self.name = name
        self._time = dt.strptime(prepare_time, '%H:%M').time()
        self.portions = portions

    @property
    def time(self):
        return f'{self._time:%H ч %M мин}'

    def __str__(self):
        return (f'{self.name}\n'
                f'\tПорции: {self.portions}\n'
                f'\tВремя приготовления: {self.time}\n'
                f'\tИнгридиенты: {super().__str__()[1:-1]}')


borsch = Recipe('Борщ', 6, potato='350g', prepare_time='1:30')
pelmeni = Recipe('Пельмени', 12, '2:15', **{'тесто': '1 кг', 'фарш': '2 кг'})
print(borsch)
print(pelmeni)

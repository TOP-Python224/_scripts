class Table:
    def __init__(self,
                 length: int,
                 width: int,
                 height: int,
                 material: str):
        self.length = length
        self.width = width
        self.height = height
        self.material = material

    def __str__(self):
        return f'<{self.material} Table: {self.length}x{self.width}x{self.height}>'


class ComputerTable(Table):
    def __init__(self,
                 length: int,
                 width: int,
                 height: int,
                 material: str,
                 keyboard_panel: bool):
        # явное обращение к методу родительского класса
        # Table.__init__(self, length, width, height, material)
        # предпочтительное обращение к методу родительского класса
        super().__init__(length, width, height, material)
        # добавление дополнительного атрибута экземпляра
        self.keyboard_panel = keyboard_panel


ct1 = ComputerTable(1650, 800, 750, 'ЛДСП', True)
print(ct1)
print(ct1.__dict__)

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @property
    def area(self) -> int:
        return self.width * self.height


rc1 = Rectangle(3, 5)
print(f'{rc1.area = }')

rc1.width = 6
print(f'{rc1.area = }')

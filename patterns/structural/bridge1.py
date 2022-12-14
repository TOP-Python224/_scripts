"""Демонстратор моста."""

from abc import ABC, abstractmethod


# Raster Vector
# Square Circle Triangle Cat

# геометрический рост количества сущностей
# RasterSquare VectorSquare RasterCircle VectorCircle ...

# composition over inheritance — ассоциация предпочтительнее наследования


class Renderer(ABC):
    """
    Интерфейс для вывода объектов.
    """
    @abstractmethod
    def render_square(self, side: float):
        pass

    @abstractmethod
    def render_circle(self, radius: float):
        pass

    # def render_triangle


class RasterRenderer(Renderer):
    """
    Реализация интерфейса для вывода объектов в растровом виде.
    """
    def render_square(self, side: float):
        print(f'pixels for the square of side {side}')

    def render_circle(self, radius: float):
        print(f'pixels for the circle of radius {radius}')

    # def render_triangle


class VectorRenderer(Renderer):
    """
    Реализация интерфейса для вывода объектов в векторном виде.
    """
    def render_square(self, side: float):
        print(f'line for the square of side {side}')

    def render_circle(self, radius: float):
        print(f'line for the circle of radius {radius}')

    # def render_triangle


class Shape(ABC):
    """
    Абстрактный базовый класс для объектов, которые требуется выводить с использованием какого-либо интерфейса.
    """
    def __init__(self, renderer_obj: Renderer):
        # экземпляр реализации интерфейса
        self.renderer = renderer_obj

    @abstractmethod
    def draw(self):
        """Выводит объект."""

    @abstractmethod
    def resize(self, factor: float):
        """Изменяет размер объекта."""


class Square(Shape):
    def __init__(self, renderer_obj: Renderer, side: float):
        super().__init__(renderer_obj)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor: float):
        self.side *= factor


class Circle(Shape):
    def __init__(self, renderer_obj: Renderer, side: float):
        super().__init__(renderer_obj)
        self.radius = side

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor


rr = RasterRenderer()
vr = VectorRenderer()

shapes = [
    Square(rr, 5),
    Square(vr, 5),
    Circle(vr, 2.8)
]
for shape in shapes:
    shape.draw()
print()

shapes[-1].renderer = rr
shapes[-1].draw()

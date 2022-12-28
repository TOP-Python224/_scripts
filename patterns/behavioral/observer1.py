class Camera:
    """Наблюдатель."""
    _id: int = 0

    def __init__(self, name: str):
        self.id = self._id
        self.__class__._id += 1
        self.name = name

    def __hash__(self):
        return self.id

    def make_photo(self):
        """Реакция наблюдателя."""
        print(f'фото с камеры {self.name}')


class CameraSystem:
    """Наблюдаемый объект."""
    def __init__(self):
        self.cameras: set[Camera] = set()

    def connect(self, camera: Camera):
        """Подписка наблюдателя на наблюдаемый объект."""
        self.cameras.add(camera)

    def disconnect(self, camera: Camera):
        """Отписка наблюдателя на наблюдаемый объект."""
        self.cameras.remove(camera)

    def notify_observers(self):
        """Уведомление всех наблюдателей (подписчиков) о событии."""
        for observer in self.cameras:
            observer.make_photo()


terminal = CameraSystem()

cam1 = Camera('Юго-Восток')
cam2 = Camera('Восток')
cam3 = Camera('Северо-Запад')

for cam in (cam1, cam2, cam3):
    terminal.connect(cam)

# звонок в дверь
terminal.notify_observers()

terminal.disconnect(cam2)

# звонок в дверь
terminal.notify_observers()


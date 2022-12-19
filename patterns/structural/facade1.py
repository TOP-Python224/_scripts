class CPU:
    @staticmethod
    def start():
        print('CPU: starting')

    @staticmethod
    def cool():
        print('CPU cooler: started')


class RAM:
    @staticmethod
    def load(data: str):
        print('RAM: data is loaded')


class Drive:
    @staticmethod
    def read(address: int):
        print(f'Drive: data from {address:#x} is read')

    @staticmethod
    def write(data: bytes):
        print('Drive: data is written')


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.drive = Drive()

    def start(self):
        self.cpu.cool()
        self.cpu.start()
        self.ram.load(self.drive.read(30))


pc = Computer()
pc.start()

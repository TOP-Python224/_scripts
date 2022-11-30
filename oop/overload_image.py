from pathlib import Path
from sys import path

group_dir = Path(path[0]).parent.parent


class Image:
    def __init__(self, binary_data: bytes):
        self.binary_date = binary_data

    def __contains__(self, subimage: bytes):
        return subimage in self.binary_date


portrait = Image((group_dir / 'logo.jpg').read_bytes())
print(portrait.binary_date)

face = '1F78'
print(face in Image)


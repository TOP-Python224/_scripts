def print_align(text: str, 
                right: bool = False) -> None:
    pass

print_align(text='test')
print_align(text='test', right=True)

# приведёт к исключению в коде функции из-за того, что аргументы запишутся в не предназначенные для них параметры
# print_align(True, 'test')
# корректная передача аргументов
print_align(right=True, text='test')

# приведёт к исключению во время вызова функции
# print_align(right=True, 'test')
# корректная передача аргументов
print_align('test', right=True)



from datetime import datetime as dt
from pathlib import Path

def write_song_in_db(file_object: bytes,
                     title: str,
                     artist: str,
                     album: str = None,
                     year: int = dt.now().year,
                     file_type: str = 'WAV',
                     sample_rate: int = 44100,
                     bit_depth: int = 24) -> bool:
    pass

song_file = Path('./mysong.mp3')
song_object = song_file.read_bytes()

write_song_in_db(song_object, 
                 'My Song', 
                 'Me',
                 'Me and Co',
                 file_type=song_file.suffix[1:].upper(),
                 bit_depth=16)

write_song_in_db(title='My Song 2', 
                 artist='Me',
                 album='Me and Co',
                 file_object=song_object, 
                 file_type=song_file.suffix[1:].upper(),
                 bit_depth=16)

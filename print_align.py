from shutil import get_terminal_size as gts

terminal_width = gts()[0] - 1

def print_align(text: str, 
                right: bool = False) -> None:
    """Выводит в стандартный поток текст, выравнивая его влево или вправо по ширине окна терминала."""
    if right:
        if len(text) < terminal_width:
            margin = ' '*(terminal_width - len(text))
    else:
        margin = ''
    print(margin + text)


print_align('test')
print_align('test', True)

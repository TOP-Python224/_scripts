def function_name(pos1, pos2, /, pos_or_key, *, key1, key2):
    print(locals())

# приведёт к исключению: строго ключевые переданы позиционно
function_name(1, 2, 3, 4, 5)

# корекктно
function_name(1, 2, 3, key1=4, key2=5)
function_name(1, 2, pos_or_key=3, key1=4, key2=5)

# приведёт к исключению: строго позиционные переданы по ключу
function_name(pos1=1, pos2=2, pos_or_key=3, key1=4, key2=5)

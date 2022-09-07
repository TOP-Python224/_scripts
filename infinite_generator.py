def repeater(obj):
    while True:
        yield obj


gen_obj = repeater(5)
for elem in gen_obj:
    print(elem, end=' ')



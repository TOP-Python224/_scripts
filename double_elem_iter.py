from typing import Iterable

def double_elem_iter(elements: Iterable):
    for elem in elements:
        yield elem
        yield elem


gen_obj = double_elem_iter([1, 2, 3, 4, 5])
for n in gen_obj:
    print(n, end=' ')

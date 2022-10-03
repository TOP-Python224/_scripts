from typing import Iterable


def flat_recur(container: Iterable) -> list:
    result = []
    for elem in container:
        # if isinstance(elem, (tuple, list, dict, set, ...)):
        if isinstance(elem, Iterable) and not isinstance(elem, str):
            result += flat_recur(elem)
        else:
            result += [elem]
    return result


data = [
    1, 2, 3, 
    ('a', 'b'), 
    5, 
    [
        (0.1, 0.2, 0.3), 
        (
            {'AB': 123, 'CD': 456}, 
            {10: 'x', 11: 'y', 12: 'z'}
        )
    ]
]
# flattening -> [1, 2, 3, 'a', 'b', 5, 0.1, 0.2, 0.3, 'AB', 'CD', 10, 11, 12]

data_flat = flat_recur(data)
print(data_flat)

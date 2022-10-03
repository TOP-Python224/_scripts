from json_examples import data
from typing import Iterable
from pprint import pprint


def all_nested_keys(obj: dict) -> tuple:
    result = ()
    for key, value in obj.items():
        result += (key, )
        if isinstance(value, dict):
            result += all_nested_keys(value)
    return result


def all_nested_values(container: Iterable) -> tuple:
    result = ()
    if isinstance(container, dict):
        for value in container.values():
            if isinstance(value, Iterable):
                result += all_nested_values(value)
            else: 
                result += (value, )
    elif isinstance(container, str):
        result += (container, )
    elif isinstance(container, Iterable):
        for elem in container:
            if isinstance(elem, Iterable):
                result += all_nested_values(elem)
            else:
                result += (elem)
    return result



# pprint(all_nested_keys(data))
pprint(all_nested_values(data))

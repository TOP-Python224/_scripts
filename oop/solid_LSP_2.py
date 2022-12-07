"""Liskov Substitution Principle — Принцип Подстановки Лисков"""

class DictOfRanges(dict):
    def __getitem__(self, item):
        if isinstance(item, int):
            for left, right in self:
                if left <= item <= right:
                    return super().__getitem__((left, right))
        else:
            return super().__getitem__(item)


d = DictOfRanges({
    (0, 13): 'abc',
    (14, 15): 'e',
    (16, 19): 'fg'
})
print(d)
print(d[4], d[14], d[17])

print(d[(0,13)])

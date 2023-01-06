class Test:
    def __repr__(self):
        return 'машиночитаемое строковое представление'

    def __str__(self):
        return 'человекочитаемое строковое представление'


t = Test()
print(t)

print(f'{t!s}\n{t!r}')

class UserError(Exception):
    def __init__(self, number: int):
        super().__init__(f'user exception about issue {number}')

class UserCertainError(UserError):
    pass


def test_raise(arg1):
    # ...
    int(arg1)
    # ...
    # raise UserError(3)
    raise UserCertainError(3)


try:
    test_raise(7)
except UserError as e:
    print(e)
    print(e.__class__)

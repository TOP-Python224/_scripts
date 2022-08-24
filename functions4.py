def test_func(*args, kw_arg1=' ', kw_arg2='\n'):
    print(f'{type(args) = }{kw_arg2}{args = }{kw_arg2}')

test_func(1, 10, 'abc')
test_func()
test_func([1, 4, 90, 3, 1])



# KeyWord ARGumentS
def test_func2(*args, **kwargs):
    print(f'{type(args) = }\n{args = }\n')
    print(f'{type(kwargs) = }\n{kwargs = }\n')

test_func2(1, [2.1, 2.2, 2.3, 2.4], 3, 
           key1=10, new=20, flag=False)

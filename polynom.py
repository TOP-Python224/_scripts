# a*x**3 + b*x**2*y + c*x*y**2 + d*y**3 + e = ?

def polynom(x: str,
            y: str,
            *,
            a: str = '1', 
            b: str = '0', 
            c: str = '0', 
            d: str = '1', 
            e: str = '0') -> float:
    args = locals().copy()
    for par, arg in args.items():
        args[par] = float(arg)
    return (
        args['a'] * args['x']**3
        + args['b'] * args['x']**2 * args['y']
        + args['c'] * args['x'] * args['y']**2
        + args['d'] * args['y']**3
        + args['e']
    )


res = polynom('1', '2.2', a='3', b='4', c='5.5', d='6.6', e='7')

print(f'{res = }')

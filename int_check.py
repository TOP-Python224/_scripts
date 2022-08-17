while True:
    inp, n = input('число: '), None
    
    for ch in inp:
        if ch not in '0123456789':
            print(' _ строка содержит лишние символы!')
            break
    else:
        print(' _ строка содержит только цифры')
        n = int(inp)
    
    print(n, type(n))
    
    if n is not None:
        break

while True:
    comm = input(' > ')
    # if comm == 'exit' or comm == 'quit':
    if comm in ('exit', 'quit'):
        break
    elif comm == 'line':
        print('='*40, end='\n\n')
    elif comm == 'square':
        print('='*40)
        for _ in range(18):
            print('=' + ' '*38 + '=')
        print('='*40, end='\n\n')

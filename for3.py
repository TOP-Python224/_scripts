from itertools import repeat

# while True:
    # inp = input(' > ')
    # if inp == 'quit':
        # break
    # else:
        # print(f"\t{inp.upper()}")

for _ in repeat(None):
    inp = input(' > ')
    if inp == 'quit':
        break
    else:
        print(f"\t{inp.upper()}")

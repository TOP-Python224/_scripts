# нахождение наибольшего общего делителя
while True:
    n = input('n: ')
    if not n:
        break
    else:
        n = int(n)
    m = int(input('m: '))
    n, m = min(n, m), max(n, m)

    while mod := m % n:
        print(f"{m = }\t{n = }\t{mod = }")
        m, n = n, mod
    print(f"greatest common divider = {n}")

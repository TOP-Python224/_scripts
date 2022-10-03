# 2**5 -> 2**4 * 2 -> 2**3 * 2 * 2 -> 2**2 * 2 * 2 * 2 -> 2 * 2 * 2 * 2 * 2

def pow_recur(base: int, exp: int) -> int:
    print(f'pow_recur: {base = } {exp = }')
    if exp > 1:
        res = base * pow_recur(base, exp-1)
        print(f'pow_recur -> {res}')
        return res
    else:
        print(f'pow_recur -> {base}')
        return base


print(pow_recur(2, 5))
# (((((2) * 2) * 2) * 2) * 2)

# stdout:
# pow_recur: base = 2 exp = 5
# pow_recur: base = 2 exp = 4
# pow_recur: base = 2 exp = 3
# pow_recur: base = 2 exp = 2
# pow_recur: base = 2 exp = 1
# pow_recur -> 2
# pow_recur -> 4
# pow_recur -> 8
# pow_recur -> 16
# pow_recur -> 32

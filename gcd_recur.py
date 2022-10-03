def gcd(number1: int, number2: int) -> int:
    
    def gcd_recur(n1: int, n2: int) -> int:
        print(f'gcd_recur: {n1 = } {n2 = }')
        if n2 > 0:
            res = gcd_recur(n2, n1%n2)
            print(f'gcd_recur -> {res}')
            return res
        else:
            print(f'gcd_recur -> {n1}')
            return n1
    
    print(locals())
    
    return gcd_recur(max(number1, number2), 
                     min(number1, number2))


print(gcd(28, 1024))


# stdout:
# gcd_recur: number1 = 1024 number2 = 28
# gcd_recur: number1 = 28 number2 = 16
# gcd_recur: number1 = 16 number2 = 12
# gcd_recur: number1 = 12 number2 = 4
# gcd_recur: number1 = 4 number2 = 0
# gcd_recur -> 4
# gcd_recur -> 4
# gcd_recur -> 4
# gcd_recur -> 4
# gcd_recur -> 4

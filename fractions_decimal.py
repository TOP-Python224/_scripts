from fractions import Fraction as F
from decimal import Decimal as D
from math import pi

f1 = F(12, 15)
f2 = F(f1)
f3 = F(0.25)
f4 = F(D('0.01'))
f5 = F('1/7')

print(f1, f2, f3, f4, f5, sep='\n')

print(f'\n{f5.numerator = }')
print(f'{f5.denominator = }\n')

print(pi)
pi_fraction = F(pi)
print(f'{pi_fraction = }')

print(f'\n{pi_fraction.limit_denominator(1000) = }\n'
      f'{float(pi_fraction.limit_denominator(1000))}')

print(f'\n{pi_fraction.limit_denominator(100) = }\n'
      f'{float(pi_fraction.limit_denominator(100))}')

print(f'\n{pi_fraction.limit_denominator(10) = }\n'
      f'{float(pi_fraction.limit_denominator(10))}')



print(f'\n\n{D(0.1) = }')
print(f'{D("0.1") = }')
print(f'{D("0.1") == 0.1 = }')

nums = [D('0.1'), D('0.3'), D('0.13'), D('0.2'), D('0.7'), D('0.9')]
print(f'\n{sum(nums) = }')

print(f'\n{D("0.1") + 1 = }')
print(f'{D("0.5")**2 = }')

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.13
# 分数类型
import fractions

x = fractions.Fraction(1, 3)
print(x)  # 1/3

y = fractions.Fraction(4, 6)
print(y)  # 2/3
print(x + y)  # 1
print(x - y)  # -1/3
print(x * y)  # 2/9
print(x / y)  # 1/2

# Fraction + int->Fraction
# Fraction + float->float
print(x + 2)  # 7/3
print(x + 2.0)  # 2.3333333333333335
print(x + 1/3)  # 0.6666666666666666

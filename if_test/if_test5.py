# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.6
# 数字零
from decimal import Decimal
from fractions import Fraction

if 0:
    print("0 is truth value")
else:
    print("0 is not truth value")

if 0.0:
    print("0.0 is truth value")
else:
    print("0.0 is not truth value")

if 0j:
    print("0j is truth value")
else:
    print("0j is not truth value")

if Decimal(0):
    print("Decimal(0) is truth value")
else:
    print("Decimal(0) is not truth value")

if Fraction(0, 1):
    print("Fraction(0, 1) is truth value")
else:
    print("Fraction(0, 1) is not truth value")

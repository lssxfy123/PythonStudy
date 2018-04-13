# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.13
# 小数对象
import decimal
decimal.getcontext().prec = 4  # 设置全局精度
print(decimal.Decimal(1) / decimal.Decimal(7))  # 0.1429
print(decimal.Decimal(199) + decimal.Decimal(1.33333))  # 200.3

# 设置块的精度
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal(1) / decimal.Decimal(7))  # 0.14

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.13
# 数字

# / 除法返回结果总是浮点数
# floor除法//如果操作数有浮点数，
# 则结果为浮点数，否则为整数
print(10 / 4)  # 2.5
print(10 / 5)
print(10 / 4.0)  # 2.5
print(10 // 4)  # 2，floor除法
print(10 // 4.0)  # 2.0
print(1 / 3)  # 0.3333333333333333
print('{0:4.2f}'.format(1 / 3))  # 0.33

# 复数
print(2 + 1j * 3)  # (2+3j)

# 八进制、十六进制、二进制
print(0o377)  # 255
print(0xFF)  # 255
print(0b11111111)  # 255
print()
print(oct(64))  # 0o100
print(hex(64))  # 0x40
print(bin(64))  # 0b1000000

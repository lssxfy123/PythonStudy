# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.13
# 位运算
x = 0b0001
print(x)

# 左移
print(x << 2)  # 4
print(bin(x << 2))  # 0b100

# 或
print(bin(x | 0b010))  # 0b11

# 与
print(bin(x & 0b1))  # 0b1

# 非
x = 0xff
print(bin(x ^ 0b10101010))  # 0b01010101

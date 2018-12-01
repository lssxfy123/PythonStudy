# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.1
# 浮点数运算

# 在Python中，多个浮点数相加会产生意外的情况
# 这是由于在Python中存储0.1的值为其近似值，
# 多个浮点数相加就会产生一些微小的误差
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004
# print(len(835))  # error, 不支持整型
# print(0 + "5")  # error
s1 = "hello"
print(s1[-3:])  # 最后3个

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)  # [1, 2, 3, [4, 5, 6]]

a1 = [1, 2, 3]
b1 = [4, 5, 6]
a1 = a1 + b1
print(a1)  # [1, 2, 3, 4, 5, 6]

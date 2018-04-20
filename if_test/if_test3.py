# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.19
# 真值测试
t1 = 2 < 3, 3 < 2
print(t1)  # (True, False)

# and和or会返回对象，
# 不是左侧，就是右侧
# or运算符从左至右计算，
# 返回第1个为真的对象
# 如果没有真值，就返回最后的对象
t2 = 2 or 3, 3 or 2
print(t2)  # (2, 3)
t3 = [] or 3
print(t3)  # 3
t4 = [] or {}
print(t4)  # {}

# and运算符从左至右计算，
# 停在第1个为假的对象上，
# 如果都为真，返回最后一个对象
t5 = 2 and 3, 3 and 2
print(t5)  # (3, 2)
t6 = [] and {}
print(t6)  # []
t7 = 3 and []
print(t7)  # []

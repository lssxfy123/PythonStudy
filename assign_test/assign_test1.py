# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.17
# 赋值
spam, ham = 'yum', 'YUM'  # 元组赋值，按位置从左到右匹配
print(spam, ham)  # yum YUM
[spam1, ham1] = ['yum', 'YUM']  # 列表赋值，按位置从左到右匹配
print(spam1, ham1)  # yum YUM

# 序列赋值，从左到右匹配
# 包含了元组赋值和列表赋值
# 字符串也是序列
# 如果无法匹配就会报错
a, b, c, d = 'spam'
print(a, b, c, d)  # s p a m
# a, b, c = 'spam'  # Error

# 即使左右两边类型不一致，
# 也支持序列赋值
[a2, b2, c2] = (1, 2, 3)
print(a2, b2, c2)  # 1 2 3

# 扩展的序列解包
# 第一个字符s匹配a1
# 剩下的赋值给b1
a1, *b1 = 'spam'
print(a1, b1)  # s ['p', 'a', 'm']

# 增强赋值，在原处修改，
# 对于不变对象，
# 与spams = spams + 42没有区别
# 不变对象不支持原处修改
# 对于可变对象，在原处修改，会影响
# 到其他相关的变量，相当于list1.append
spams = 0
hams = spams
spams += 42
print(spams)  # 42
print(hams)  # 0
print()
list1 = [1, 2, 3]
list2 = list1
list1 += [4, 5, 6]
print(list1)  # [1, 2, 3, 4, 5, 6]
print(list2)  # [1, 2, 3, 4, 5, 6]

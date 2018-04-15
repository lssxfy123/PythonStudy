# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 元组
t1 = ('abc', ('def', 'ghi'))
# t1[0] = 'xxx'  # Error，不可变对象，不支持原处修改
t2 = tuple('spam')
print(t2[1:3])
x = (40,)  # 单个元素的元组，逗号不能省略，否则会变成整数40
print(x)  # (40,)

# 忽略元组的()
t3 = 0, 'Ni', 1.2, 3
print(t3)  # (0, 'Ni', 1.2, 3)
print()

a, b, c, d = 0, 'Ni', 1.2, 3
print(a, b, c, d)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.17
# 列表切片赋值与扩展序列解包
L1 = [1, 2, 3, 4]
print('original L1', L1)  # original L1 [1, 2, 3, 4]
# 元组不能如此赋值，不支持原处修改
L1[1:3] = [8, 9]
print('after assign', L1)  # after assign [1, 8, 9, 4]
print()

# 扩展序列解包
# 不仅支持列表，也支持其他序列类型
seq = [1, 2, 3, 4]

# a = 1, b = [2, 3, 4]
a, *b = seq
print('a = {0}, b = {1}'.format(a, b))

# a1 = [1, 2, 3], b1 = 4
*a1, b1 = seq
print('a1 = {0}, b1 = {1}'.format(a1, b1))

# a2 = 1, b2 = [2, 3], c2 = 4
a2, *b2, c2 = seq
print('a2 = {0}, b2 = {1}, c2 = {2}'.format(a2, b2, c2))

# 边界情况
# a3 = 1, b3 = 2, c3 = 3, d3 = [4]
# d3是一个列表
a3, b3, c3, *d3 = seq
print('a3 = {0}, b3 = {1}, c3 = {2}, d3 = {3}'.format(a3, b3, c3, d3))

# a4 = 1, b4 = 2, c4 = 3, d4 = 4, e4 = []
# e4是一个空列表
a4, b4, c4, d4, *e4 = seq
print('a4 = {0}, b4 = {1}, c4 = {2}, d4 = {3}, e4 = {4}'
      .format(a4, b4, c4, d4, e4))

# a5 = 1, b5 = 2, c5 = 3, d5 = 4, e5 = []
a5, b5, *e5, c5, d5 = seq
print('a5 = {0}, b5 = {1}, c5 = {2}, d5 = {3}, e5 = {4}'
      .format(a5, b5, c5, d5, e5))
# a5, b5, *e5, c5, *d5 = seq  # Error，*只能有1个
# *a5 = seq  #Error *必须在列表或元组中
*a6, = seq
print('a6 = {0}'.format(a6))  # a6 = [1, 2, 3, 4]

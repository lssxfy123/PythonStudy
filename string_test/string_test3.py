# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 字符串切片扩展
s = 'abcdefghijklmnop'

# 从2取到10，步长为2
# 取1,3,5,7,9
print(s[1:10:2])  # bdfhj

s1 = 'hello'
# 负值步长，从尾到头
print(s1[::-1])  # olleh

s2 = 'abcdefg'
# 取值范围为cdef，从右至左
#步长为2
print(s2[5:1:-2])  # fd

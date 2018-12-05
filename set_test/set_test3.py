# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.5
# 集合中的函数
s1 = set([3, 1, 2, 4.5])
print(s1.pop())  # 删除s1中的一个元素，随机的，因为集合没有顺序

s2 = set([3, 1, 2, 4.5])
s3 = set([3, 11, 22, 33, 4.5])
s4 = s2.union(s3)  # 并集
print(s4)  # {1, 2, 3, 4.5, 33, 11, 22}

s5 = s2.intersection(s3)  # 交集
print(s5)  # {3, 4.5}

s6 = s2.difference(s3)  # s2中在s3没有的
print(s6)  # {1, 2}

s7 = s3.difference(s2)  # s3中在s2没有的
print(s7)  # {33, 11, 22}

# 集合中可以包含不同类型的元素
# 但是与list类似，使用某些函数
# 时有可能会出现Error
s8 = {1, 2, 3, 'spam'}
print(s8)

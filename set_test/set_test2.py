# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 集合
# 集合只能包含不可变(可散列的)对象类型
s = {1.23}
# s.add([1, 2, 3])  # Error, not list
# s.add({'a': 1})  # Error, not dict
s.add((1, 2, 3))
print(s)  # {1.23, (1, 2, 3)}

# 集合本身是可变对象
s1 = {1, 2, 3}
# s2 = {4, 5, s1}  # Error, not set
s2 = {4, 5, frozenset(s1)}
print(s2)  # {frozenset({1, 2, 3}), 4, 5}
print()

# 集合不支持下标访问
# print(s1[0])  # Error
for item in s2:
    if isinstance(item, frozenset):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)


def set_changeable(set1):
    set1.add(3)


s3 = {1, 2}
print('original set: ', s3)  # {1, 2}
set_changeable(s3)
print('set_changealbe set: ', s3)  # {1, 2, 3}

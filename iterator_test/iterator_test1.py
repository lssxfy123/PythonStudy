# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.22
# 迭代器
from collections import Iterable

# 可迭代对象
l1 = [1, 2, 3]
t1 = (1, 2)
d1 = {'a': 1, 'b': 2}
s1 = 'abc'
set1 = {1, 2, 3}
print(isinstance(l1, Iterable))  # True
print(isinstance(t1, Iterable))  # True
print(isinstance(d1, Iterable))  # True
print(isinstance(s1, Iterable))  # True
print(isinstance(set1, Iterable))  # True
print()

# 文件迭代器
# 通过迭代的方式按行读取
# 不要把整个文件都加载到内存中
# 效率比使用readLines()要高
with open('data.txt') as file_obj:
    for line in file_obj:  # 调用file_obj.__next()__并catch StopIteration
        print(line, end='')
print()
print()

# 手动迭代
L = [1, 2, 3]
it1 = iter(L)
print(it1.__next__())  # 1
print(it1.__next__())  # 2
print(it1.__next__())  # 3
# print(it1.__next__())  # StopIteration

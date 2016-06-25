#for循环的迭代
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print("name is ", name)

#dict的for循环迭代
d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

#默认迭代key值
for key in d:
    print('key', key)

#迭代value值
for value in d.values():
    print('value', value)

#迭代key-value值
for key, value in d.items():
    print('key,', key, 'value', value)

#字符串的for循环迭代
for ch in 'abcdefg':
    print('ch', ch)

#判断一个对象是否可以进行迭代
from collections import Iterable
print('字符串是否可以迭代', isinstance('abcdefg', Iterable))
print('list是否可以迭代', isinstance([1, 2, 3], Iterable))
print('整数是否可以迭代', isinstance(123, Iterable))

#类似C++中的下标方式的for循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#两个变量的for循环
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print('x', x, 'y', y)
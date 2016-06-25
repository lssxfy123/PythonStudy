#迭代器
#可迭代的对象不一定是一个迭代器，而迭代器一定是可迭代的
#可以使用next()函数调用不不断返回下一个值的对象称为迭代器
from collections import Iterator, Iterable

print("generator is iterable", isinstance((x for x in range(10)), Iterable))
print("list is iterable", isinstance([], Iterable))
print("dict is iterable", isinstance({}, Iterable))
print("str is iterable", isinstance('abc', Iterable))
print('int is iterable', isinstance(10, Iterable))

print("generator is iterator", isinstance((x for x in range(10)), Iterator))
print("list is iterator", isinstance([], Iterator))
print("dict is iterator", isinstance({}, Iterator))
print("str is iterator", isinstance('abc', Iterator))

#迭代器的计算时惰性计算，只有需要返回下一个数据时，才会计算

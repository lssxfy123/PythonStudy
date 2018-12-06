# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.6
# python练习测试3:函数
egg_count = 0
t1 = (1, 2)
t1 += (3,)
print(t1)
l1 = [1, 2]
l1 += [3]
print(l1)


# 在函数中不能对全局变量进行复合运算
def buy_eggs():
    print()
    # l1 += [3]  # error
    # t1 += (1,)  # error
    # egg_count += 12  # error


buy_eggs()


# 实现enumerate函数
def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


d1 = {'a': 1, 'b': 2}
for i, j in my_enumerate(d1, 0):
    print(i, j)

# 输出为：0 a
#        1 b


# 每次输出一个可迭代对象的一部分
def chunker(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]



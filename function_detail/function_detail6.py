# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.24
# 通用最小值函数


def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *args):
    for arg in args:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min1(3, 4, 1, 2))  # 1
print(min2('bb', 'aa'))  # aa
print(min3([2, 2], [1, 1], [3, 3]))  # [1, 1]

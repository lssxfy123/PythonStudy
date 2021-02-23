# Copyright(C) 2021 刘珅珅
# Environment: python 3.6.4
# Date: 2021.2.23
# 生成器的应用

_pinyin = {'hou', 'zeng', 'ben', 'xia', 'pao', 'lei'}

# 生成器，使用yield关键字
# 调用函数时，返回一个迭代器对象


def all_pinyin():
    for _ in _pinyin:
        yield _
    print("pinyin done!")


strs = "zhuang"

# if in 作用在生成器上
# 如果条件不为True，会一直迭代生成器，直到生成器结束
# 判断strs是否在生成器上，其实就是判断strs是否在_pinyin里
# 使用生成器，不用耗费大量的内存


if strs in all_pinyin():
    print(strs, ": ok")

strs = "la"
# 调用一次all_pinyin()会产生一个新的生成器
if strs in all_pinyin():
    print(strs, ": ok")

strs = "ben"
if strs in all_pinyin():
    print(strs, ": ok")

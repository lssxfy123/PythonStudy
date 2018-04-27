# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.23
# 参数传递与参数解包


# 可变参数
# 可变参数是一个元组
def args(*params):
    print(isinstance(params, tuple))


args(1)  # True
args({'a': 1})  # True


# 任意关键字参数
# 任意关键字参数是一个字典
def args1(**key_words):
    print(isinstance(key_words, dict))


args1(a=1, b=2)  # True


def func(a, b, c, d):
    print('a = {0}, b = {1}, c = {2}, d = {3}'.format(a, b, c, d))


args = (1, 2, 3, 4)
# func(args)  # 参数不匹配
# 使用*运算符解包成可变参数
# 参数个数需要匹配
func(*args)  # Ok a = 1, b = 2, c = 3, d = 4

keyWords = {'a': 1, 'b': 2, 'd': 4, 'c': 3}
keyWords1 = {'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4}
# 使用**解包成任意关键字参数
# 注意：字典的keys需要与函数
# 参数名对应并且个数匹配
# 顺序可以不同
func(**keyWords)
# func(**keyWords1)  # Error

# *与**的混合运用
func(*(1, 2), **{'d': 5, 'c': 4})  # a = 1, b = 2, c = 4, d = 5
func(1, *[2, 3], **{'d': 6})  # a = 1, b = 2, c = 3, d = 6
func(1, c=99, *(2, ), **{'d': 101})  # a = 1, b = 2, c = 99, d = 101
func(1, **{'d': 101, 'b': 99}, c=0)  # a = 1, b = 99, c = 0, d = 101

# **解析为关键字参数，后面不能再跟位置参数
# func(1, **{'d': 101, 'b': 99}, 0)  # Error

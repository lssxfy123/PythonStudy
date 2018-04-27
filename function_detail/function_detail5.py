# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.24
# 命名关键字参数


# *后的b和c均为命名关键字参数
# 如果没有默认值，就必须使用关键字参数赋值
def kwonly1(a, *, b, c):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


kwonly1(1, b=2, c=3)  # a = 1, b = 2, c = 3
# kwonly1(4, 5, b=5)  # Error


# 有可变参数，不需要单独的*
def kwonly2(a, *b, c, d=5):
    print('a = {0}, b = {1}, c = {2}, d = {3}'.format(a, b, c, d))


kwonly2(1, c=8)  # a = 1, b = (), c = 8, d = 5
kwonly2(6, 6, c=8, d=9)  # a = 6, b = (6,), c = 8, d = 9

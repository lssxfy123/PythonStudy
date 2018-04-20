# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.20
# for循环扩展序列的赋值
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

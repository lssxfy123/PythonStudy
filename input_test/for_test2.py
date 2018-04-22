# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.20
# for循环扩展序列的赋值

# a = 1, b = [2, 3], c = 4
# a = 5, b = [6, 7], c = 8
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

# a1 = 1, b1 = [], c1 = 2, d1 = 3, e1 = 4
# a1 = 5, b1 = [], c1 = 6, d1 = 7, e1 = 8
for (a1, *b1, c1, d1, e1) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print('a1 = {0}, b1 = {1}, c1 = {2}, d1 = {3}, e1 = {4}'.format(a1, b1, c1, d1, e1))

s = 'abcdefghijk'
for i in range(0, len(s), 2):
    print(s[i], end=' ')  # a c e g i k
print()
print()

# zip函数
# 取得一个或多个序列为参数返回元组
# 并将并排的元素配置成对
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L3 = list(zip(L1, L2))
print(L3)  # [(1, 5), (2, 6), (3, 7), (4, 8)]

s1 = 'abc'
s2 = 'lssxfy'
s3 = list(zip(s1, s2))
print(s3)  # [('a', 'l'), ('b', 's'), ('c', 's')]

keys = ['spam', 'eggs', 'toast']
values = [1, 3, 5]

dict1 = dict(zip(keys, values))
print(dict1)  # {'spam': 1, 'eggs': 3, 'toast': 5}

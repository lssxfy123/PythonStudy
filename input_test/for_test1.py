# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.20
# for循环详解
for x in ['spam', 'eggs', 'ham']:
    if x == 'eggs':
        print("Have eggs")
        break
else:
    print("Not have eggs")
print()

# for循环遍历序列
L = [(1, 2), (3, 4), (5, 6)]
for (a, b) in L:
    print('a = {0}, b = {1}'.format(a, b))
print()

for ((a1, b1), c1) in [((1, 2), 3), ((4, 5), 6)]:
    print('a1 = {0}, b1 = {1}, c1 = {2}'.format(a1, b1, c1))
print()

# 嵌套的序列结构可以按照赋值的方式在for循环解包
for ((a2, b2), c2) in [([1, 2], 3), ['XY', 6]]:
    print('a1 = {0}, b1 = {1}, c1 = {2}'.format(a2, b2, c2))

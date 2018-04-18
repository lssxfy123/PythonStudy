# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.17
# 高级序列赋值
string = 'spam'
# a, b, c = string  # Error
a, b, c = string[0], string[1], string[2:]

# a = s, b = p, c = am
print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

# a1 = s, b1 = p, c1 = am
a1, b1, c1 = list(string[:2]) + [string[2:]]
print('a1 = {0}, b1 = {1}, c1 = {2}'.format(a1, b1, c1))

# a2 = s, b2 = p, c2 = am
(a2, b2), c2 = string[:2], string[2:]
print('a2 = {0}, b2 = {1}, c2 = {2}'.format(a2, b2, c2))

# a3 = S, b3 = P, c3 = AM
((a3, b3), c3) = ('SP', 'AM')
print('a3 = {0}, b3 = {1}, c3 = {2}'.format(a3, b3, c3))

l1 = [3]
front = l1[0]
# last = l1[1]  # IndexError
last = l1[1:]  # OK，空列表[]
print(front, last)  # 3 []

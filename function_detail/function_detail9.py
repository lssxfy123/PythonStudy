# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.25
# lambda
f = lambda x, y, z: x + y + z
print(f(1, 2, 3))  # 6
print()

# lambda使用在序列中
L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for f in L:
    print(f(2))  # 4 8 16
print()

# 不带参数的lambda
D = {'already': (lambda: 2 + 2), 'got': (lambda: 2 * 4)}
print(D['got']())  # 8
print(D['already']())  # 4

lower = (lambda x, y: x if x < y else y)
print(lower('aa', 'bb'))  # aa

# 嵌套lambda，类似嵌套函数，避免使用
action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))  # 102
print(act(5))  # 104

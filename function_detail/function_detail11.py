# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.25
# 生成器函数
from collections import Iterable


# 生成器，使用yield关键字
# 调用函数时，返回一个迭代器对象
def gensquares(n):
    for i in range(n):
        yield i ** 2


# gensquares每次循环产生一个值，通过yield
# 返回给调用者，并暂停，其上一个状态保存下来，
for i in gensquares(5):
    print(i, end=':')  # 0:1:4:9:16:
print()
G = 88


def gen(n):
    global G
    G = 99
    for i in range(n):
        yield i ** 3


# 与普通函数不同，直接调用生成器函数时，
# 不会立即执行函数体的语句，其返回一个迭代器对象，
# 通过next()执行，遇到yield返回，再次通过next()执行时，
# 从上次返回的yield语句处继续执行
x = gen(4)
print(isinstance(x, Iterable))  # True
print("G =", G)  # G = 88
print(next(x))  # 0
print("G =", G)  # G = 99
print(next(x))  # 1
print(next(x))  # 8
print()


# 通过for循环遍历生成器与通过next()执行生成器是类似的
# 但如果生成器有return语句时，会有所不同
def fib(number):
    n, a, b = 0, 0, 1
    while n < number:
        yield b
        a, b = b, a + b
        n += 1
    return 'Done'


f = fib(4)
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print("Generator return message:", e.value)
        break
print()

# 通过for循环遍历生成器对象，无法得到return的内容
for i in fib(4):
    print(i)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.24
# 通用函数


# 不知道函数名和参数
def tracer(func, *args, **kargs):
    print("call func: ", func.__name__)
    return func(*args, **kargs)


def func1(a, b, c, d):
    return a + b + c + d


def func2(a, b):
    return a * b


print(tracer(func1, 1, 2, c=3, d=4))
print(tracer(func2, **{'a': 5, 'b': 6}))
print(tracer(func2, 10, *(5,)))

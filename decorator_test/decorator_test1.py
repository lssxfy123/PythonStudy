# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.26
# 函数装饰器


def log(func):
    def wrapper(*args, **kwargs):
        print('call {0}(): '.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


# Python解析为add = log(add)
# log返回函数对象wrapper
# add = wrapper
# add(x, y)等同于wrapper(x, y)
# 类似Python学习手册第17章的工厂函数
@log
def add(x, y):
    return x + y


class Sum:
    @log
    def method(self, x, y):
        return x + y


def log1(func):
    print('call {0}(): '.format(func.__name__))
    return func


# 相当于sub = log1(sub)
# log1被调用
@log1
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(add(3, 5))
    print()

    sum1 = Sum()
    print(sum1.method(4, 6))

    print(sub(1, 3))

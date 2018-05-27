# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.26
# 函数装饰器的顺序


def decorator_a(func):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a


def decorator_b(func):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b


@decorator_b
@decorator_a
def func(x):
    print('Get in func')
    return x * 2


if __name__ == '__main__':
    print(func(2))

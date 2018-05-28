# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.26
# 类作为函数装饰器


class Decorator:
    def __init__(self, func):
        print('init Decorator')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Decorator call')
        return self.func(*args, **kwargs)


@Decorator
def func(x, y):
    return x + y


if __name__ == '__main__':
    print(func(3, 5))

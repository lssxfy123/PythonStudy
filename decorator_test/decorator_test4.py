# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.27
# 类装饰器


def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            print('init Wrapper')
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print('get attr in Wrapper')
            return getattr(self.wrapped, name)
    return Wrapper


# 类装饰器
@decorator
class Spam:
    def __init__(self, x, y):
        self.attr = 'spam'
        self.x = x
        self.y = y


if __name__ == '__main__':
    a = Spam(6, 7)
    print(a.attr)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.23
# 通过type创建类


def func(self, name='world'):
    print('Hello, {0}'.format(name))


# 通过type创建类
Hello = type('Hello', (object,), dict(hello=func))


if __name__ == '__main__':
    h = Hello()
    h.hello()  # Hello, world
    print(type(h))  # <class '__main__.Hello'>
    print(type(Hello))  # <class 'type'>

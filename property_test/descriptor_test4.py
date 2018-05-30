# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.30
# 只读描述符2


class Descriptor:
    def __get__(self, instance, owner):
        print('get')

    def __set__(self, instance, value):
        raise AttributeError('can`t set')


class Test:
    attr = Descriptor()


if __name__ == '__main__':
    x = Test()
    x.attr
    # x.attr = 99  # AttributeError，can`t set
    Test.attr = 99  # 无法拦截以类属性方式赋值
    print(Test.attr)  # 99

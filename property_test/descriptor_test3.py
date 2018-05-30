# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.30
# 只读描述符


# 只有__get__不能确保只读
class Descriptor:
    def __get__(self, instance, owner):
        print('get')


class Test:
    attr = Descriptor()


if __name__ == '__main__':
    x = Test()
    x.attr
    Test.attr
    print(id(x.attr))
    x.attr = 99
    print(x.attr)  # 99，屏蔽了描述符attr，x.attr访问实例x的独有属性
    print(id(x.attr))
    Test.attr  # get
    y = Test()
    y.attr  # get

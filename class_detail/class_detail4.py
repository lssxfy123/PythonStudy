# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 运算符重载
import class_detail3


class ThirdClass(class_detail3.SecondClass):
    def __init__(self, value):
        print('__init__ called')
        self.data = value

    def __add__(self, other):
        print('__add__ called')
        return ThirdClass(self.data + other)

    def __str__(self):
        print('__str__ called')
        return '[ThirdClass: {0}]'.format(self.data)

    def mul(self, other):
        self.data *= other


if __name__ == '__main__':
    a = ThirdClass('abc')
    a.display()
    print(a)  # __str__被调用
    print()

    b = a + 'xyz'
    b.display()
    print(b)
    print()

    a.mul(3)
    print(a)

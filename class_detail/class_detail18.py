# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.23
# 元类


class MetaClassOne(type):
    def __new__(mcs, classname, superclasses, attrs):
        print('In MetaClassOne.new: ', classname, superclasses, attrs, sep='\n...')
        return type.__new__(mcs, classname, superclasses, attrs)

    def __init__(cls, classname, superclasses, attrs):
        print('In MetaClassOne.init: ', classname, superclasses, attrs, sep='\n...')


print('making class')


class Spam(metaclass=MetaClassOne):
    data = 1

    def meth(self, arg):
        pass


if __name__ == '__main__':
    print()
    print('making instance')
    x = Spam()

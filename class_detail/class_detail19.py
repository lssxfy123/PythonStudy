# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.23
# 元类的实例


class SayMetaClass(type):
    def __new__(mcs, classname, supers, attrs):
        # 在元类中根据类的名字创建一个方法
        attrs['say_' + classname] = lambda self, value, saying=classname: print(saying + ',' + value)
        return type.__new__(mcs, classname, supers, attrs)


class Hello(metaclass=SayMetaClass):
    pass


class Sayolala(metaclass=SayMetaClass):
    pass


class Nihao(metaclass=SayMetaClass):
    pass


if __name__ == '__main__':
    hello = Hello()
    # say_Hello是通过元类创建的
    hello.say_Hello('world!')  # Hello,world!

    s = Sayolala()
    s.say_Sayolala('japan!')  # Sayolala,japan!

    n = Nihao()
    n.say_Nihao('中国!')  # Nihao,中国!


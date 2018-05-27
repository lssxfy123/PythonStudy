# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.27
# 装饰器创建单例模式


class Singleton:
    def __init__(self, aClass):
        print('init Singleton')
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance


@Singleton
class Person:
    def __init__(self, name, hours, rate):
        print('init Person')
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


if __name__ == '__main__':
    print()
    print('Start Test')
    bob = Person('Bob', 40, 10)
    print(bob.name, bob.pay())
    print()
    sue = Person('Sue', 50, 20)
    print(sue.name, sue.pay())
    print('bob id', id(bob))
    print('sue id', id(sue))
    print('End test')

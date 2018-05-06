# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 实例


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):  # 运算符重载
        return '[Person: {0}, {1}]'.format(self.name, self.pay)


if __name__ == '__main__':
    bob = Person('Bob Smith', 'dev', 10000)
    print(bob.name, bob.pay)
    print(bob.last_name())
    bob.give_raise(0.1)
    print(bob.pay)
    print(bob)

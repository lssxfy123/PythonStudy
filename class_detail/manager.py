# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 实例
import person


class Manager(person.Person):
    def __init__(self, name, pay):
        super().__init__(name, 'mgr', pay)

    # 重载超类的方法，除非功能完全不同，
    # 一般尽可能使用超类的方法来扩展，
    # 以方便后序维护
    def give_raise(self, percent, bonus=0.1):
        super().give_raise(percent+bonus)


if __name__ == '__main__':
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(0.1)
    print(tom)  # 子类会继承超类的运算符重载

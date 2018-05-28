# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.25
# 静态方法


class Spam:
    instances_count = 0

    def __init__(self):
        Spam.instances_count += 1

    # 定义静态方法，不需要self
    def print_instances_count():
        print('Number of instances:', Spam.instances_count)
    print_instances_count = staticmethod(print_instances_count)


# 子类可以继承超类的静态方法
# 还可以调用超类的静态方法
class Sub(Spam):
    def print_instances_count():
        print('Extra stuff...')
        Spam.print_instances_count()
    print_instances_count = staticmethod(print_instances_count)


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()

    # 可以通过类名和实例来调用静态方法
    # 与C++类似
    Spam.print_instances_count()
    a.print_instances_count()
    print()

    d = Sub()
    d.print_instances_count()

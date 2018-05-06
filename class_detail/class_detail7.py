# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 类树


def class_tree(cls, indent):
    print('.' * indent + cls.__name__)
    for super_cls in cls.__bases__:  # 查找超类
        class_tree(super_cls, indent + 3)


def instance_tree(inst):
    print('Tree of {0}'.format(inst))
    class_tree(inst.__class__, 3)  # __class__实例的类


def test():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass

    instance_tree(B())
    instance_tree(F())


if __name__ == '__main__':
    test()

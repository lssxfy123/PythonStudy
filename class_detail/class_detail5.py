# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 类的属性


# 最简单的Python类
class Rec:
    pass


if __name__ == '__main__':
    Rec.name = 'Bob'  # 类的属性
    Rec.age = 40
    print(Rec.name)
    print(list(Rec.__dict__.keys()))
    print()

    x = Rec()
    y = Rec()
    # 实例会继承类的属性
    print(x.name, y.name)
    print(list(x.__dict__.keys()))  # []，实例本身没有属性
    print(list(y.__dict__.keys()))
    print()

    x.name = 'Sue'
    print(x.name)
    print(list(x.__dict__.keys()))  # ['name']，实例x有自身的属性name

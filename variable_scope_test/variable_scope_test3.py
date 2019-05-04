# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 嵌套作用域
x = 99


# f2()中的x就位于嵌套作用域内
# 但不允许在f2()修改x，只能访问
def f1():
    x = 88

    def f2():
        # x -= 66  # 不能修改
        print('f2() x: ', x)
    f2()


f1()

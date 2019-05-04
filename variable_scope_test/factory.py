# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 嵌套作用域：工厂函数


def maker(n):
    def action(p):
        return p ** n
    return action


f = maker(2)  # f是函数对象，可以调用action函数
g = maker(3)
print(f)
print(f(3))  # 9 3 ** 2
print(f(4))  # 16 4 ** 2
print()
print(g)
print(g(3))  # 27 3 ** 3

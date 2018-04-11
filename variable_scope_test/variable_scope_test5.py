# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# nonlocal语句：在函数内部赋值嵌套作用域的变量


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


f = tester(0)
f('spam')  # spam 0
f('ham')  # ham 1
f('egg')  # egg 2
print()

g = tester(42)
g('spam')  # spam 42
g('ham')  # ham 43
g('egg')  # egg 44

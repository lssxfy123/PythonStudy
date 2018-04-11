# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# global语句：在函数内部赋值全局变量
x = 88


# 外部之前未定义，直接
# 在函数内部使用global z
# 调用函数后，z也可以在外部使用
def func():
    global x
    x = 99
    global z
    z = 100


func()
print('x = ', x)
print('z = ', z)

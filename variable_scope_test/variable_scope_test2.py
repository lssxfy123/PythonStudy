# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 本地作用域
x = 99


def func(y):
    z = x + y
    return z


func(0)
# print(z, y)  # Error，z, y为定义


languages = ['English', 'Chinese']


# 在函数内部以任何方式赋值一个变量，该变量都会
# 被设定为本地变量，但在函数内部修改了一个对象
# 则不会把变量划分为本地变量
# func_1()中的x是本地变量，与全局的x互不影响
# languages是全局变量
def func_1():
    x = 8
    languages.append('Russia')
    print("func_1 x = ", x)
    print("func_1 languages id ", id(languages))


func_1()
print('x = ', x)
print('languages id ', id(languages))

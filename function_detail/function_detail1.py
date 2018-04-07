# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.7
# 函数名与函数对象


def pets(pet):
    print("pet is", pet)


# 函数名pets是一个变量，
# 其引用了一个函数对象
# 将其赋值给pets_1后，
# 可以通过pets_1调用函数
pets_1 = pets
pets_1('cat')

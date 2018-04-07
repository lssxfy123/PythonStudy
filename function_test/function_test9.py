# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.7
# 参数组合


# 位置参数与可变参数的组合
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
# make_pizza(size=16, topping='pepperoni')  # 可变参数无法使用关键字
print()


# python中参数的组合与顺序
# c为默认参数
def parameter_sequence1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)


# c为命名关键字参数
# 如果参数中有可变参数，就不需要
# 使用*来定义命名关键字参数
def parameter_sequence2(a, b, *args, c=0, **kw):
    print('a = ', a, 'b = ', b, 'args = ', args, 'c = ', c, 'kw = ', kw)


parameter_sequence1(1, 2)
parameter_sequence1(1, 2, c=3)
parameter_sequence1(1, 2, 3, 'a', 'b', key=99)
print()
parameter_sequence2(1, 2, 'a', 'b', c=99, key=1001)
parameter_sequence2(1, 2, 'a', 'b', x=99, key=1001)

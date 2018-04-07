# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.7
# 任意长度的参数：可变参数


def make_pizza(*toppings):
    # 可变参数是一个元组
    if isinstance(toppings, tuple):
        print("toppings is tuple")
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
print()
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print()


def calc_sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result


print(calc_sum(1, 2))
print(calc_sum(1, 2, 3))

# 如果存在一个列表或元组
# 可以使用*将其转换为可变参数
nums_1 = [1, 2, 3, 4, 5]
nums_2 = (1, 3, 5, 7, 9)
print(calc_sum(*nums_1))
print(calc_sum(*nums_2))

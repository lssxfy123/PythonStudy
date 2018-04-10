# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.8
# 函数模块


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

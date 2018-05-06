# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.5
# 类和实例


class Dog:
    def __init__(self, name, age):

        self.name = name
        self.__age = age


my_dog = Dog('哈士奇', 2)
print(type(Dog))
print(type(my_dog))
print(id(Dog))
print(id(my_dog))

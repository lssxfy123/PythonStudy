# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 类


class Dog:
    def __init__(self, name, age):
        """初始化"""
        # 类中定义了两个属性，类似C++中的成员变量
        # name是public，前面加__是private
        # 类中所有的属性必须提供初始值
        self.name = name
        self.__age = age

    # 函数第一个参数永远是self
    def sit(self):
        print(self.name.title() + " is now sitting")


my_dog = Dog("willie", 6)
your_dog = Dog("Tom", 7)
my_dog.sit()
your_dog.sit()
print(my_dog.name)
# print(my_dog.__age)  # Error

# 可以给类的实例绑定属性
# 但只有该实例可用
my_dog.weight = 9
print(my_dog.weight)
print()
# print(your_dog.weight)  # Error，没有weight属性


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 默认值

    def get_descriptive_name(self):
        full = str(self.year) + ' ' + self.make + ' ' + self.model
        return full.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back an odometer!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

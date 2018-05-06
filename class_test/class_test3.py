# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 重写父类的方法


# 父类
class Car:
    def fill_gas_tank(self):
        print("This car has fill gas")


# 子类重写了父类的方法
# 如果通过子类对象调用方法
# 就会调用子类的方法
class ElectricCar(Car):
    def fill_gas_tank(self):
        print("This car doesn't need gas")


my_car = Car()
my_car.fill_gas_tank()

my_tesla = ElectricCar()
my_tesla.fill_gas_tank()

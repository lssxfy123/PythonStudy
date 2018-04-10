# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 类的继承


# 基类
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


# 子类
# 基类__init__的参数，子类
# 最好也有，否则有可能出现错误
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        print("init electric car")

    def describe_battery(self):
        print("This car has a" + str(self.battery_size) + "-kWh battery")


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.read_odometer()
my_tesla.describe_battery()

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# car类模块


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


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            battery_range = 240
        elif self.battery_size == 85:
            battery_range = 280

        message = "This car can go approximately " + str(battery_range)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # 类的实例做为属性
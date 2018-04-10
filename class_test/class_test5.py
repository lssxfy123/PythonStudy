# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 导入类模块
import car
from car import Car

# 使用car中的类时需要添加模块名car.
my_tesla = car.ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

my_car = Car('audi', 'a4', 2017)
print(my_car.get_descriptive_name())

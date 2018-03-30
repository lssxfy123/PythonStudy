# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.3.30
# 条件测试
cars = ['audi', 'bmw', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car == 'bmw')
        print(car.upper())
    else:
        print(car.title())
print()

# 判断不相等
age = 18
if age != 42:
    print("That is not the answer")

# 多条件判断
# 与：and
if 16 <= age and 20 >= age:
    print("Age is ok")

# 或：or
if 15 <= age or 25 >= age:
    print("Age is ok")

# 判断是否在列表中
print('audi' in cars)

print('toyota' in cars)

# 判断是否不在列表中
if 'toyota' not in cars:
    print('you can add toyota')

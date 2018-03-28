# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Create Date: 2018.3.28
# 列表

bicycles = ['trek', 'redline']
print(bicycles[0])

# 修改
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# 添加
# 队尾添加
motorcycles.append("honda")
print(motorcycles)

# 插入
motorcycles.insert(1, 'lifan')
print(motorcycles)

# 删除
del motorcycles[0]
print(motorcycles)

# 删除队尾
motorcycles.pop()
print(motorcycles)

motorcycles.pop(1)
print(motorcycles)

# 根据元素值删除
# 删除第一个匹配值
# 如果不存在会报错
motorcycles.remove('lifan')
print(motorcycles)
print()

# 列表排序
cars = ['bmw', 'audi', 'toyota', 'ford']
print("original:")
print(cars)
cars.sort()
print("sort:")
print(cars)
print()

# 临时排序
cars1 = ['bmw', 'audi', 'toyota', 'ford']
print("original:")
print(cars1)
print("sorted:")
print(sorted(cars1))
print("original again:")
print(cars1)

# 获取列表长度
length = len(cars1)
print("length: ")
print(length)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.3
# 模块导入

# 将small.py模块赋值给small变量
import small

# 将small.py模块中的x,y赋值给本地的x,y
from small import x, y
print(type(small))
print()
print("x id in module_test2.py", id(x))
print("y id in module_test2.py", id(y))
print("original x", x)
print("original y", y)
x = 42  # 不变对象
print("x id ", id(x))
print("small.x = ", small.x)
print("small.x id ", id(small.x))
y[0] = 42  # 可变对象
print("small.y = ", small.y)

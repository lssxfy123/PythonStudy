# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.4
# 数据隐藏

# import hide
# print("x ", hide.x)  # ok, 6
# print("_x ", hide._x)  # ok, 5

# from hide import _x
# print("_x ", _x)  # ok, 5

from hide import *
print("x ", x)  # ok, 6
# print("_x ", _x)  # NameError: name '_x' is not defined

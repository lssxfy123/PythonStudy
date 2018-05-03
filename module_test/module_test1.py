# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.27
# 模块搜索路径
import sys
import sum  # PYTHONPATH
import sub  # PYTHONPATH
import multiply  # .pth文件
import divide  # .pth文件
print("path: ", sys.path)
print(sum.sum1(1, 2))
print(sub.sub1(1, 2))
print(multiply.multiply1(2, 3))
print(divide.divide1(5, 2))

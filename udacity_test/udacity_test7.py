# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.7
# python练习测试7：模块测试
import math
import random
import datetime
from udacity_test5 import func
from udacity_test6 import func  # 不同模块的同名函数，后导入的会将之前的覆盖掉
print(math.pow(math.e, 3))

words = ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]
print(random.sample(words, 3))

func()


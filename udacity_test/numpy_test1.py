# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.12
# Numpy练习1
import numpy as np
import time

t1 = (1, 'a')
l1 = [1, 'a']
d1 = {'k': 1, 2: 'd'}  # key的类型可以不同，value类型也可以不同
print(t1)
print(l1)
print(d1)

# NumPy计算效率与Python比较
x = np.random.random(100000000)

# 计算平均值
start = time.time()
sum(x) / len(x)
print(time.time() - start)  # 11.726816654205322s

np_start = time.time()
np.mean(x)
print(time.time() - np_start)  # 0.20415043830871582s

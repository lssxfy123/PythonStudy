# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.11.14
# 训练与测试模型
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
data = np.array(data)
x = data[:, 0:2]
y = data[2]

print(x)

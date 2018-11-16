# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.11.14
# 学习曲线
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
data = np.array(data)
X = data[:, 0:2]
y = data[:, 2]

# 随机打乱样本数据
# 根据y的长度length(y为一维数组)得到[0:length]
# 然后将这个列表中元素的顺序随机打乱生成permutation
permutation = np.random.permutation(y.shape[0])
# print(y.shape[0])
# print(permutation)
# 将X和y根据这个随机的索引顺序进行随机打乱顺序
X2 = X[permutation, :]
y2 = y[permutation]
# print(y2)

# 线性逻辑回归
estimator = LogisticRegression()

# 学习曲线
# 其中输入参数train_sizes为训练样本的相对或绝对数量
# 如果为整数代表绝对数量，浮点数代表选用的相对数量
train_sizes_abs, train_scores, test_scores\
    = learning_curve(estimator, X2, y2, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 10))

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.grid()

plt.title("Learning Curves")
plt.xlabel("Training examples")
plt.ylabel("Score")

plt.plot(train_scores_mean, 'o-', color="g",
         label="Training score")
plt.plot(test_scores_mean, 'o-', color="y",
         label="Cross-validation score")

plt.legend(loc="best")

plt.show()

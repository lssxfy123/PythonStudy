# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.11.14
# 训练与测试模型
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

data = pd.read_csv('data.csv')
data = np.array(data)
X = data[:, 0:2]
y = data[:, 2]

# 逻辑回归
classifier = LogisticRegression()
classifier.fit(X, y)

# SVM
classifier = SVC()
classifier.fit(X, y)

# 决策树
classifier = DecisionTreeClassifier()
classifier.fit(X, y)


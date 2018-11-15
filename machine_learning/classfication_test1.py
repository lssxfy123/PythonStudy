# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.10.30
# 分类学习：线性分类
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

# 创建特征列表
column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']

# 读取数据
data = pd.read_csv('https://archive.ics.uci.edu/ml/'
                   'machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', names=column_names)

# 将缺省值?替换为NumPy的标准缺失值
data = data.replace(to_replace='?', value=np.nan)
data = data.dropna(how='any')

# 将数据保存成csv文件，不加行索引
# data.to_csv('total.csv', index=False)

# print(data.shape)

# 数据分割，多少训练，多少预测
# data[column_names[1:10]]：样本特征集
# data[column_names[10]]：样本标签集
# X_train：训练特征集
# y_train：训练标签集
# X_test：测试特征集
# y_test：测试标签集
X_train, X_test, y_train, y_test = \
    train_test_split(data[column_names[1:10]], data[column_names[10]], test_size=0.25, random_state=33)

# 第1列为Excel列号+1
# 第2列为'Class'列的值
# print(y_train)

# 标准化数据，每个维度的特征数据方差为1，均值为0
# 会将每个维度的数据标准为正负值
ss = StandardScaler()

# 将数据类型转换为float
X_train = X_train.astype(float)
X_test = X_test.astype(float)
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

LR = LogisticRegression()
SGDC = SGDClassifier()

# 调用LogisticRegression来训练模型
LR.fit(X_train, y_train)

# LR预测
lr_y_predict = LR.predict(X_test)

# 输出概率
lr_proba = LR.predict_proba(X_test)

# 调用SGDClassifier来训练模型
SGDC.fit(X_train, y_train)

# SGDC预测
sgdc_y_predict = SGDC.predict(X_test)

# 结果分析
# LR
print('Accuracy of LR Classifier: ', LR.score(X_test, y_test))
print(classification_report(y_test, lr_y_predict, target_names=['Benign', 'Malignant']))

print('\n')

# SGDC
print('Accuracy of SGDC Classifier: ', SGDC.score(X_test, y_test))
print(classification_report(y_test, sgdc_y_predict, target_names=['Benign', 'Malignant']))

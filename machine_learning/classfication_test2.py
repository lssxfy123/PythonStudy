# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.10.30
# 分类学习：支持向量机
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# 通过数据加载器获取手写数字的数码图像
digits = load_digits()
# print(digits.data.shape)

# 样例切割
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=3)

# 数据标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# 线性假设的支持向量机分类
LSVC = LinearSVC()

# 模型训练
LSVC.fit(X_train, y_train)

# 预测
y_predict = LSVC.predict(X_test)

# 评价
print('The Accuracy of Linear SVC is ', LSVC.score(X_test, y_test))
print()
print(classification_report(y_test, y_predict, target_names=digits.target_names.astype(str)))

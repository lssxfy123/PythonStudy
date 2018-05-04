# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.4
# 包相对导入
# 该py文件不能直接运行
# 只能发生在包内
# 只能使用from语句
from .add import add  # 相对导入
print("add()", add(1, 2))

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.3
# 模块删除
import small
print("module id", id(small))  # module id 202670467256
print("delete module")
del small
# print(small.y)  # Error，name 'small' is not defined

import small  # 不会重新执行导入
print("module id", id(small))  # module id 202670467256

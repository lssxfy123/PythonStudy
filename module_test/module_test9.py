# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.5
# import和from语句的as扩展
import small as sm
from name import tester as func

# as扩展之后，只能使用as之后的变量名来引用该模块
# print(small.x)  # Error，无法使用small
print(sm.x)

# tester()  # Error
func()

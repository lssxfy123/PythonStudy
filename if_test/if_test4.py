# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.19
# if/else三元表达式
# 相当于
# if 'spam':
#    a = 't'
# else:
#    a = 'z'
a = 't' if 'spam' else 'z'
print(a)  # t

n = 8 if 0 else 9
print(n)  # 9

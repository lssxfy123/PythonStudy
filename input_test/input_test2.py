# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.3
# 输入

# int()将字符串转换为数字
age = input('How old are you? ')
age = int(age)
print('Greater than 18:' + str(age >= 18))

# 求模运算符
# 参考https://baike.baidu.com/item/%E5%8F%96%E6%A8%A1%E8%BF%90%E7%AE%97/10739384?fr=aladdin
# 除数是正，余数也为正
# 除数是负，余数也为负
print(-5 % 3)  # 1
print(5 % 3)  # 2
print(5 % -3)  # -1
print(-5 % -3)  # -2

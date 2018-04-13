# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 字符串序列操作
str1 = 'Spam'
print(len(str1))
print(str1[0])
print(str1[-1])  # 最后一个
print(str1[-2])  # 倒数第2个
print()

# 字符串切片
print(str1[1:3])  # pa
print(str1[1:])  # pam
print(str1[:-1])  # Spa
print(str1[:])  # Spam

print(str1 + 'xyz')  # Spamxyz
print(str1 * 2)  # SpamSpam

# 字符串为不可变对象
# str1[0] = 'z'  # Error

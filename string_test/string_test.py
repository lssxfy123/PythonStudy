# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.3.27
str1 = "This is python"
str2 = 'This is python too'

# 修改大小写
name = "ada lovelace"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

# 删除空白
language = " python "

# 删除头部空白
language = language.lstrip()

# 删除尾部空白
language = language.rstrip()

# 删除两端空白
language = language.strip()

# 将数字解读为字符串
age = 23
birthday = "Hello " + str(age) + "rd birthday"
print(birthday)


# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.15
# 字符串格式化：老版
# Python中的格式化类似C语言中的格式化
x = 1234
print('integers:...%d...' % x)  # integers:...1234...

# -6d，从左对齐，小于6位，用空格补足低位
print('integers:...%-6d...' % x)  # integers:...1234  ...

# 06d，小于6位，高位补0
print('integers:...%06d...' % x)  # integers:...001234...

y = 1.23456789
# -6.2f，小数点后保留2位有效数字，从左对齐，小于6位，用空格补足低位
print('integers:...%-6.2f...' % y)  # integers:...1.23  ...

# 05.2f，小数点后保留2位，小于5位，高位补0
print('integers:...%05.2f...' % y)  # integers:...01.23...
print()

# 基于字典的格式化
reply = """Greetings...
Hello %(name)s!
Your age squared is %(age)s"""
values = {'name': 'Bob', 'age': 40}
print(reply % values)

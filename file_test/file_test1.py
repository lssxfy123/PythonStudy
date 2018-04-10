# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 文件读取

# 读取整个文件
# 通过with访问文件不需要手动关闭
with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents)

print()

# 读取二进制文件
with open('画板.png', 'rb') as file_binary:
    print(file_binary.read())


# 以指定编码方式读取文件
with open('..\gbk.txt', 'r', encoding='gbk') as file_gbk:
    print(file_gbk.read())
print()

# 逐行读取
# 打印结果每行之间有空白行
# 这是打印换行符造成的
# 可以使用rstrip()清除换行符
with open('pi.txt') as file_line:
    for line in file_line:
        print(line.rstrip())
print()

# 按行读取这个文件
with open('pi.txt') as file_lines:
    lines = file_lines.readlines()

for content in lines:
    print(contents.rstrip())

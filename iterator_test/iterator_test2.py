# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.22
# 列表解析的扩展
# 解析文件
lines = [line.rstrip().upper() for line in open('data.txt')]
print(lines)  # ['ABC', '123', 'PYTHON', 'HELLO, WORLD']

# 嵌套解析
s = [x + y for x in 'abc' for y in 'lmn']
print(s)  # ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']

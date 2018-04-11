# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# json读取
import json

file_name = 'info.json'

# 通过json读取json文件后的结果转换为了字典
# 普通文件读取结果为字符串
with open(file_name, 'r') as file_object:
    user_info = json.load(file_object)
print(isinstance(user_info, dict))  # True

for key, value in user_info.items():
    print(key, ":", value)

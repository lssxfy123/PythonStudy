# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# json写入
import json

numbers = [2, 3, 5, 7, 11, 13]
file_name = 'numbers.json'
with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)

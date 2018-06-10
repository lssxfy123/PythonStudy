# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# .通配符
import re

if __name__ == '__main__':
    # .匹配除换行之外的任意字符
    regex = re.compile(r'.at')  # 除换行符外，任意字符后跟at都匹配
    result = regex.findall('The cat in the hat sat on the flat matlab')
    # .通配符只匹配1个字符
    print(result)  # ['cat', 'hat', 'sat', 'lat', 'mat']

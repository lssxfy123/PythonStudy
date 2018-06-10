# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# *匹配
import re

if __name__ == '__main__':
    # *匹配0次或多次
    regex = re.compile(r'Bat(wo)*man')
    result = regex.search('The Adventures of Batman')
    print(result.group())

    result = regex.search('The Adventures of Batwoman')
    print(result.group())

    result = regex.search('The Adventures of Batwowowoman')
    print(result.group())

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# 正则表达式初探
import re

if __name__ == '__main__':
    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    text1 = 'My number is 415-555-4242'
    text2 = 'My number is 18811751156'
    text3 = 'My number is 415-5555-424'

    result = regex.search(text1)
    if result:
        print(result.group())
    else:
        print('Not match regular')

    result = regex.search(text2)
    if result:
        print(result.group())
    else:
        print('Not match regular')

    result = regex.search(text3)
    if result:
        print(result.group())
    else:
        print('Not match regular')

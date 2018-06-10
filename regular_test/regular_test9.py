# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# ^和$
import re

if __name__ == '__main__':
    regex = re.compile(r'^Hello')
    result = regex.search('Hello, world!')
    print(result.group())  # Hello

    result = regex.search('aHello, world!')
    print(result)  # None
    print()

    regex = re.compile(r'\d$')
    result = regex.search('Number is 42')
    print(result.group())  # 2

    result = regex.search('Number is two')
    print(result)  # None

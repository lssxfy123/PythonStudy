# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# ?匹配
import re

if __name__ == '__main__':
    # ?表示wo为可选匹配
    regex = re.compile(r'Bat(wo)?man')
    result = regex.search('The Adventures of Batman')
    print(result.group())  # Batman

    result = regex.search('The Adventures of Batwoman')
    print(result.group())  # Batwoman
    print()

    regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    result = regex.search('My number is 415-555-4242')
    print(result.group(0))  # 415-555-4242
    print(result.group(1))  # 415-
    print()

    result = regex.search('My number is 555-4242')
    print(result.group())  # 555-4242

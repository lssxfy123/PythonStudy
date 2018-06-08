# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# |管道匹配
import re

if __name__ == '__main__':
    # 匹配许多表达式中的1个
    regex = re.compile(r'Batman|Tina')
    text = 'aaa Batman and Tina'
    result = regex.search(text)
    print(result.group())  # Batman

    text = 'Tina and Batman'
    result = regex.search(text)
    print(result.group())  # Tina

    regex = re.compile(r'Bat(man|mobile|copter|bat)')
    text = 'aaaa Batmobile lost a wheel'
    result = regex.search(text)
    print(result.group())  # Batmobile

    text = 'aaaa Batman lost a wheel'
    result = regex.search(text)
    print(result.group())  # Batman

    text = 'aaaa Batcopter lost a wheel'
    result = regex.search(text)
    print(result.group())  # Batcopter

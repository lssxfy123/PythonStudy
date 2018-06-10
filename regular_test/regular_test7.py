# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# {}匹配
import re

if __name__ == '__main__':
    # {}匹配特定次数
    regex = re.compile(r'Bat(wo){3}man')  # 匹配3次
    result = regex.search('The Adventures of Batwowowoman')
    print(result.group())  # Batwowowoman

    result = regex.search('The Adventures of Batwowoman')
    print(result)  # None
    print()

    regex = re.compile(r'Bat(wo){3,5}man')  # 匹配3-5次
    result = regex.search('The Adventures of Batwowowoman')  # 3次
    print(result.group())  # Batwowowoman

    result = regex.search('The Adventures of Batwowowowoman')  # 4次
    print(result.group())  # Batwowowowoman

    result = regex.search('The Adventures of Batwowowowowowoman')
    print(result)  # None
    print()

    regex = re.compile(r'Bat(wo){3,}man')  # 匹配3次及以上
    result = regex.search('The Adventures of Batwowowoman')  # 3次
    print(result.group())  # Batwowowoman

    result = regex.search('The Adventures of Batwowowowoman')  # 4次
    print(result.group())  # Batwowowowoman

    result = regex.search('The Adventures of Batwowowowowowoman')  # 6次
    print(result.group())  # Batwowowowowowoman
    print()

    regex = re.compile(r'Bat(wo){,5}man')  # 匹配0-5次
    result = regex.search('The Adventures of Batwowowoman')  # 3次
    print(result.group())  # Batwowowoman

    result = regex.search('The Adventures of Batwowowowoman')  # 4次
    print(result.group())  # Batwowowowoman

    result = regex.search('The Adventures of Batman')  # 0次
    print(result.group())  # Batman

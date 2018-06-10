# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# findall:所有匹配
import re

if __name__ == "__main__":
    # 无分组，返回字符串列表
    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print(regex.findall('Cell: 415-555-9999 Word: 212-555-0000'))

    # 有分组
    regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    print(regex.findall('Cell: 415-555-9999 Word: 212-555-0000'))

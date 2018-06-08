# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.8
# ()匹配
import re

if __name__ == '__main__':
    regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    text1 = 'My number is 415-555-4242'
    result = regex.search(text1)
    print(result.group(0))  # 415-555-4242
    print(result.group(1))  # 415
    print(result.group(2))  # 555
    print(result.group(3))  # 4242
    print()

    # 文本中包含()
    text2 = 'My number is (415)-555-4242'
    regex1 = re.compile(r'(\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)')
    result = regex1.search(text2)
    print(result.group(1))  # (415)
    print(result.group(2))  # 555
    print(result.group(3))  # 4242

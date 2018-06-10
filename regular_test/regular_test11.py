# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# .*匹配
import re

if __name__ == '__main__':
    # .*贪心匹配：匹配尽可能多的字符
    regex = re.compile(r'<.*>')
    result = regex.search('<To sever man> fro dinner>')
    print(result.group())  # <To sever man> fro dinner>

    # .*非贪心匹配：匹配尽可能少的字符
    regex = re.compile(r'<.*?>')
    result = regex.search('<To sever man> fro dinner>')
    print(result.group())  # <To sever man>

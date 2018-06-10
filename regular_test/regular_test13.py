# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# 正则实现strip()
import re


def re_strip(text, del_char=r'\s'):
    regex_format = r'^{0}*|{1}*$'.format(del_char, del_char)
    regex = re.compile(regex_format)
    text = regex.sub('', text)
    return text


if __name__ == '__main__':
    print(re_strip('aadasdfaaa', 'a'))  # dasdf
    print(re_strip('   dafas   '))  # dafas


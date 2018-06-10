# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.10
# 强口令检查
import re

if __name__ == '__main__':
    text = 'aaL12222222'
    if len(text) >= 8:
        have_number = False
        regex = re.compile(r'\d+')
        result = regex.search(text)
        if result:
            regex = re.compile(r'[a-z]+')
            result = regex.search(text)
            if result:
                regex = re.compile(r'[A-Z]+')
                result = regex.search(text)
                if result:
                    print('Ok')
                else:
                    print('Not have upper char')
            else:
                print('Not have lower char')
        else:
            print('Not have number')
    else:
        print('length must >= 8')

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 异常记录
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


# 记录异常信息
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('End')

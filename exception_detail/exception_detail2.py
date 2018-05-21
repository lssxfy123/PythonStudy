# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.12
# 异常处理try-except-finally
from exception_detail1 import fetcher

x = 'spam'


def after():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception')
        return  # 即使except有return语句，也会执行finally块，与C#类似
    finally:
        print('after fetcher')


if __name__ == '__main__':
    after()

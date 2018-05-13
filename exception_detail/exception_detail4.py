# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.12
# 基于类的异常


class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    x = General()
    raise x


def raiser1():
    x = Specific1()
    raise x


def raiser2():
    x = Specific2()
    raise x


if __name__ == '__main__':
    for func in (raiser0, raiser1, raiser2):
        try:
            func()
        except General:  # 捕获超类异常，可以捕获继承其的所有子类异常
            import sys
            print('caught:', sys.exc_info()[0])

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 异常抛出


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()

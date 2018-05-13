# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.12
# 异常的嵌套


def action():
    print(1 + [])


try:
    try:
        action()
    except TypeError:
        print('inner try')
except TypeError:
    print('outer try')

try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.9
# 代理池异常


class PoolEmptyError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')

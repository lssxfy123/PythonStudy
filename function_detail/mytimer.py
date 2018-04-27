# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.26
# 模块计时
import time
reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return elapsed, ret

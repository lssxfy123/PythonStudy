# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.27
# 模块计时测试
import sys, mytimer
reps = 10000
repslist = range(reps)


def for_loop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def list_comp():
    return [abs(x) for x in repslist]


def map_call():
    return list(map(abs, repslist))


def gen_expr():
    return list(abs(x) for x in repslist)


def gen_fun():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)
for test in (for_loop, list_comp, map_call, gen_expr, gen_fun):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s.....%s]' %
          (test.__name__, elapsed, result[0], result[-1]))

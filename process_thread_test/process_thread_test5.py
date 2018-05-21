# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.20
# 多线程传递类对象
import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc:
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        # 运算符重载
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def test():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        thread = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(thread)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    test()

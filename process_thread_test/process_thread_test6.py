# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.20
# 自定义线程
import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
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
        thread = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(thread)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    test()

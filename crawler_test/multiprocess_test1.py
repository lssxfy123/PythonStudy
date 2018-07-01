# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.30
# 多进程爬虫
import multiprocessing
import os


def run_proc(name):
    print('Child process {0} {1} Running'.format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print('process start')
        p.start()
    p.join()
    print('Process close')

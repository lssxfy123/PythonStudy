# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.20
# 进程
import os
from multiprocessing import Process


def run_process(name):
    print('Run child process {0} ({1})'.format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {0}.'.format(os.getpid()))
    child = Process(target=run_process, args=('test',))
    print('Child Process will start.')
    child.start()  # 启动进程
    child.join()  # 等待子进程执行完毕在
    print('Child process end.')

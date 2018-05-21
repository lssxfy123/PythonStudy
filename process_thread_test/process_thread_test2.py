# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.20
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random


def write(queue):
    print('Process to write: {0}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put {0} to queue...'.format(value))
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    print('Process to read: {0}'.format(os.getpid()))
    while True:
        value = queue.get(True)
        print('Get {0} from queue.'.format(value))


if __name__ == '__main__':
    q = Queue()
    process_write = Process(target=write, args=(q,))
    process_read = Process(target=read, args=(q,))
    process_write.start()
    process_read.start()
    process_write.join()
    process_read.terminate()

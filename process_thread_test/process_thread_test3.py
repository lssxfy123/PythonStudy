# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.20
# 多线程
import threading

balance = 0
lock = threading.Lock()


def change(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000):
        lock.acquire()  # 加锁
        try:
            change(i)
        finally:
            lock.release()  # 释放锁


if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)  # 0

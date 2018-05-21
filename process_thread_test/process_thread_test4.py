# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.20
# ThreadLocal
import threading

# 全局ThreadLocal对象
# local_school为全局对象
# 但其属性为线程的局部对象
# 可以在多线程中任意读写而互不干扰
local_school = threading.local()


def get_student():
    # 获取当前线程关联的student
    student = local_school.student
    print('Hello, {0} (in {1})'.format(student, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    get_student()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

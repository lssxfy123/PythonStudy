# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.12
# 异常处理try-except
x = 'spam'


def fetcher(obj, index):
    return obj[index]


def test():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception')
    print('test end')  # 发生异常也会执行到这里


if __name__ == '__main__':
    test()

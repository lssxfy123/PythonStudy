# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.31
# 多线程访问网站
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen

regex = compile(r'图书商品里排第([\d,]+)')
amazon = 'https://amazon.cn/dp/'
isbns = {'0132269937': 'Core Python Programming'}


def get_ranking(isbn):
    url = '{0}{1}'.format(amazon, isbn)
    page = uopen(url)
    data = page.read()
    page.close()
    # print(type(data))
    # 将data转换为str
    data1 = data.decode('utf-8')

    result = regex.search(data1)
    # print(result)
    return result.group(1)


def show_ranking(isbn):
    print('- %r ranked %s' % (isbns[isbn], get_ranking(isbn)))


def test():
    print('At', ctime(), 'on Amazon...')
    for isbn in isbns:
        Thread(target=show_ranking, args=(isbn,)).start()


@register
def my_exit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    test()

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.30
# 多进程爬取10000个URL
import requests
from lxml import etree
import pymongo
from multiprocessing import Pool
from mongodb_test import mongo_port
from mongodb_test import mongo_host
from crawler_test1 import headers
import time

client = pymongo.MongoClient(mongo_host, mongo_port)
mydb = client['mydb']
jianshu = mydb['jianshu']


def get_jianshu(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    # 获取总的标签
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        try:
            author = info.xpath('div/div[1]/a/text()')[0]
            title = info.xpath('div/a/text()')[0]
            content = info.xpath('div/p/text()')[0].strip()
            comment = info.xpath('div/div[1]/a[2]/text()')[0]
            like = info.xpath('div/div[1]/span[1]/text()')[0].strip()
            detailed_url = "http://www.jianshu.com" + info.xpath('a[1]/@href')[0]
            time = get_time(detailed_url)

            data = {
                'author': author,
                'title': title,
                'time': time,
                'content': content,
                'comment': comment,
                'like': like
            }
            jianshu.insert_one(data)
        except IndexError:
            pass


def get_time(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    time = selector.xpath('//span[@class="publish-time"]/text()')[0]
    return time


if __name__ == '__main__':
    urls = ['http://www.jianshu.com/c/bDHhpk?order_by=added_at&page={0}'.format(str(i)) for i in range(1, 1001)]
    start1 = time.time()
    for url in urls:
        get_jianshu(url)
    end1 = time.time()
    print('串行爬虫', end1 - start1)

    start2 = time.time()
    pool = Pool(processes=4)
    for url in urls:
        pool.apply_async(get_jianshu, args=(url,))
    pool.close()
    pool.join()
    end2 = time.time()
    print('四个进程', end2 - start2)

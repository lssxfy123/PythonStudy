# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.1
# 异步爬虫
# 爬取简书7日热门
import requests
from lxml import etree
import pymongo
from mongodb_test import mongo_host
from mongodb_test import mongo_port
from crawler_test1 import headers
import re
import json
from multiprocessing import Pool

client = pymongo.MongoClient(mongo_host, mongo_port)
mydb = client['mydb']
sevenday = mydb['sevenday']


def get_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        get_info(article_url_part)


def get_info(url):
    url_header = 'https://www.jianshu.com/'
    article_url = url_header + url
    html = requests.get(article_url, headers=headers)
    selector = etree.HTML(html.text)
    author = selector.xpath('//span[@class="name"]/a/text()')[0]
    article = selector.xpath('//h1[@class="title"]/text()')[0]
    date = selector.xpath('//span[@class="publish-time"]/text()')[0]
    word = selector.xpath('//span[@class="wordage"]/text()')[0]
    view = re.findall('"views_count":(.*?),', html.text, re.S)[0]
    comment = re.findall('"comments_count":(.*?),', html.text, re.S)[0]
    like = re.findall('"likes_count":(.*?),', html.text, re.S)[0]
    id1 = re.findall('{"id":(.*?),', html.text, re.S)[0]
    gain_url = url_header + "notes/{0}/rewards?count=20".format(id1)
    wb_data = requests.get(gain_url, headers=headers)
    json_data = json.loads(wb_data.text)
    gain = json_data['rewards_count']  # 获取打赏数据

    include_list = []  # 专题信息
    include_urls = [(url_header + "notes/{0}/included_collections?page={1}").format(id1, str(i)) for i in range(1, 10)]
    for include_url in include_urls:
        html = requests.get(include_url, headers=headers)
        json_data = json.loads(html.text)
        includes = json_data['collections']
        if len(includes) == 0:
            pass
        else:
            for include in includes:
                include_title = include['title']
                include_list.append(include_title)

    info = {
        'author': author,
        'article': article,
        'date': date,
        'word': word,
        'view': view,
        'comment': comment,
        'like': like,
        'gain': gain,
        'include': include_list
    }
    sevenday.insert_one(info)


if __name__ == '__main__':
    urls = ['https://www.jianshu.com/trending/weekly?page={0}'.format(str(i)) for i in range(1, 6)]
    pool = Pool(processes=4)
    for url in urls:
        pool.apply_async(get_url, args=(url,))
    pool.close()
    pool.join()

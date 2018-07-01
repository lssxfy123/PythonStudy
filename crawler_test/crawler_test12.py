# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.1
# 异步加载网页爬取
import requests
from lxml import etree
import pymongo
from mongodb_test import mongo_host
from mongodb_test import mongo_port
from crawler_test1 import headers

client = pymongo.MongoClient(mongo_host, mongo_port)
mydb = client['mydb']
timeline = mydb['timeline']


def get_time_info(url, page):
    user_id = url.split('/')
    user_id = user_id[4]
    if url.find('page='):
        page += 1
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        dd = info.xpath('div/div/div/span/@data-datetime')[0]
        type = info.xpath('div/div/div/span/@data-type')[0]
        timeline.insert_one({'date': dd, 'type': type})

    # 获取max_id信息
    id_infos = selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(id_infos) > 1:
        feed_id = id_infos[-1]
        max_id = int(feed_id.split('-')[1]) - 1
        next_url = 'http://www.jianshu.com/users/{0}/timeline?max_id={1}&page={2}'.format(user_id, max_id, page)
        get_time_info(next_url, page)  # 获取下一页信息


if __name__ == '__main__':
    get_time_info('https://www.jianshu.com/users/9104ebf5e177/timeline', 1)

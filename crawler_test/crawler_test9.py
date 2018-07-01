# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.24
# 爬取豆瓣音乐TOP250并存入数据库
import pymongo
import requests
from lxml import etree
import crawler_test1
import re
import time
import mongodb_test

client = pymongo.MongoClient(mongodb_test.mongo_host, mongodb_test.mongo_port)
mydb = client['mydb']
music_top = mydb['musictop']


def get_url_music(url):
    html = requests.get(url, headers=crawler_test1.headers)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//a[@class="nbg"]/@href')
    for music_href in music_hrefs:
        get_music_info(music_href)


def get_music_info(url):
    html = requests.get(url, headers=crawler_test1.headers)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    author = re.findall('表演者:.*?>(.*?)</a>', html.text, re.S)[0]
    styles = re.findall('流派:.*?>(.*?)<br />', html.text, re.S)
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].replace('&nbsp;', '').strip()

    time = re.findall('发行时间:</span>(.*?)<br />', html.text, re.S)[0].strip().replace('&nbsp;', '')
    publishers = re.findall('出版者:</span>(.*?)<br />', html.text, re.S)
    if len(publishers) == 0:
        publisher = '未知'
    else:
        publisher = publishers[0].strip().replace('&nbsp;', '')

    score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]

    info = {'name': name, 'author': author, 'style': style, 'time': time, 'publisher': publisher, 'score': score}
    music_top.insert_one(info)


if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={0}'.format(str(i)) for i in range(0, 50, 25)]
    for url in urls:
        get_url_music(url)
        time.sleep(1)

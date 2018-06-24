# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.23
# 利用API获取糗事百科地址信息：经纬度
import requests
from lxml import etree
import csv
import crawler_test1
import json

fp = open('map.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('address', 'longitude', 'latitude'))


def get_user_url(url):
    url_part = 'http://www.qiushibaike.com'
    html = requests.get(url)
    selector = etree.HTML(html.text)
    url_infos = selector.xpath('//div[contains(@class,"article block untagged mb15")]')
    for url_info in url_infos:
        user_part_urls = url_info.xpath('div[1]/a[1]/@href')
        if len(user_part_urls) == 1:
            user_part_url = user_part_urls[0]
            get_user_address(url_part + user_part_url)
        else:
            pass


# 获取用户地址
def get_user_address(url):
    res = requests.get(url, headers=crawler_test1.headers)
    selector = etree.HTML(res.text)
    user_info = selector.xpath('//div[@class="user-statis user-block"]/ul/li[4]/text()')

    if len(user_info) > 1:
        address = user_info[1].split('·')
        if len(address) > 1:
            get_geo(address[1])
        elif len(address) == 1:
            get_geo(address[0])
    else:
        pass


# 利用API获取用户经纬度信息
def get_geo(address):
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    api = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(api, par)
    json_data = json.loads(res.text)

    try:
        geo = json_data['geocodes'][0]['location']
        longitude = geo.split(',')[0]
        latitude = geo.split(',')[1]
        writer.writerow((address, longitude, latitude))
    except IndexError:
        pass


if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/8hr/page/{0}/'.format(str(i)) for i in range(1, 5)]
    for url in urls:
        get_user_url(url)

    fp.close()

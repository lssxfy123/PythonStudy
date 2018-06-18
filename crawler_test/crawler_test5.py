# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.17
# Lxml解析html网页
import requests
from lxml import etree
import crawler_test1

if __name__ == '__main__':
    res = requests.get('https://book.douban.com/top250', headers=crawler_test1.headers)
    html = etree.HTML(res.text)
    result = etree.tostring(html)
    print(result)

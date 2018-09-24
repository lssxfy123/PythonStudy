# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.9
# 获取网页html
import requests
from requests.exceptions import ConnectionError

base_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/65.0.3325.181 Safari/537.36',
           'Accept-Encoding': 'gzip, deflate, sdch'}


def get_page(url, options={}):
    headers = dict(base_headers, **options)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('抓取成功', url)
            return response.text
    except ConnectionError:
        return None

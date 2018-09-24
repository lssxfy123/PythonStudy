# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.8
# 今日头条街拍
import requests
from urllib.parse import urlencode
from requests import codes
import re
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': '1',
        'from': 'search_tab'
    }

    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url)
        if codes.ok == resp.status_code:
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


def save_image(item):
    save_path = "d:/pictures/"
    image_path = save_path + re.sub('[\/:*?"<>|]', '', item.get('title'))
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            file_path = image_path + os.path.sep + '{0}.{1}'.format(md5(resp.content).hexdigest(), 'jpg')
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(resp.content)

    except requests.ConnectionError:
        print('Failed to Save Image itme {0}'.format(item))


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)


GROUP_START = 0
GROUP_END = 3
if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

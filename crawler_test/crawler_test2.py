# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.16
# 爬虫与正则匹配
# 爬取斗破苍穹小说
import requests
import re
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/65.0.3325.181 Safari/537.36'}

file_object = open('doupo.txt', 'a+')


def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:  # 请求成功
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'))
        for content in contents:
            file_object.write(content + '\n')
    else:
        pass


if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{0}.html'.format(str(i)) for i in range(1, 100)]
    for url in urls:
        get_info(url)
        time.sleep(1)

    file_object.close()

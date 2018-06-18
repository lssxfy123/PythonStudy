# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.16
# 爬虫库测试
import requests
from bs4 import BeautifulSoup
import lxml
import time

# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/65.0.3325.181 Safari/537.36'}


def get_info(url):  # 获取网页信息
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')

    for rank, title, time in zip(ranks, titles, times):
        data = {'rank': rank.get_text().strip(),
                'singer': title.get_text().split('-')[0],
                'song': title.get_text().split('-')[1],
                'time': time.get_text().strip()}
        print(data)


if __name__ == '__main__':
    # 多页url
    urls = ['http://www.kugou.com/yy/rank/home/{0}-8888.html'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        get_info(url)
        time.sleep(1)  # 休眠1秒

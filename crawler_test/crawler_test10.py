# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.30
# 多进程爬虫
import requests
import re
import time
from multiprocessing import Pool
import crawler_test1


# 获取信息的函数
def re_scraper(url):
    res = requests.get(url, headers=crawler_test1.headers)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    contents = re.findall('<div class="content">.*?</span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)
    for id1, content, laugh, comment in zip(ids, contents, laughs, comments):
        info1 = {
            'id': id1,
            'content': content,
            'laugh': laugh,
            'comment': comment
        }
    return info1


if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{0}'.format(str(i)) for i in range(1, 36)]
    start_1 = time.time()
    for url in urls:
        re_scraper(url)

    end_1 = time.time()
    print('串行爬虫', end_1 - start_1)

    start_2 = time.time()
    pool = Pool(processes=2)  # 2个进程
    for url in urls:
        pool.apply_async(re_scraper, args=(url,))

    pool.close()  # 禁止新的子进程创建
    pool.join()  # 等待所有子进程执行完毕

    end_2 = time.time()
    print('两个进程', end_2 - start_2)

    start_3 = time.time()
    pool = Pool(processes=4)  # 4个进程
    for url in urls:
        pool.apply_async(re_scraper, args=(url,))

    pool.close()
    pool.join()

    end_3 = time.time()
    print('四个进程', end_3 - start_3)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.16
# 爬虫与正则匹配
# 爬取糗事百科
import requests
import re
import time
import crawler_test1

info_lists = []


def judge_sex(sex):
    if sex == 'womenIcon':
        return '女'
    else:
        return '男'


def get_info(url):
    res = requests.get(url, headers=crawler_test1.headers)
    # 用户ID
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)  # 换行匹配
    # 用户等级
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    # 性别
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    # 内容
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    # 好笑
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    # 评论
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)

    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {'id': id, 'level': level, 'sex': judge_sex(sex), 'content': content,
                'laugh': laugh, 'comment': comment}
        info_lists.append(info)


if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/text/page/12/'
    get_info(url)
    print(info_lists)

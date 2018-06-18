# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.17
# Lxml与爬虫
# 爬取豆瓣TOP250
import requests
from lxml import etree
import crawler_test1
import csv

file_object = open('book.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(file_object)
writer.writerow(('书名', 'url', '作者', '出版社', '日期', '价格', '评分', '评论'))


# XPath语法
def get_info(url):
    html = requests.get(url, headers=crawler_test1.headers)
    selector = etree.HTML(html.text)
    # 选取所有带有class='item'属性的tr元素
    infos = selector.xpath("//tr[@class='item']")
    for info in infos:
        # 选取父元素为div，祖父元素为td的所有a元素的title属性
        # 第1个值为book name
        book_name = info.xpath('td/div/a/@title')[0]
        book_url = info.xpath('td/div/a/@href')[0]

        # 选取父元素为td的所有p元素的文本，第1个值为书籍信息
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]  # 倒数第3个
        date = book_infos.split('/')[-2]  # 倒数第2个
        price = book_infos.split('/')[-1]  # 倒数第1个

        # 选取父元素为div，祖父元素为td的第2个span元素的文本
        # 计算索引2时，属于不同div的span元素会分开计算
        rate = info.xpath('td/div/span[2]/text()')[0]

        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) > 0 else '空'

        writer.writerow((book_name, book_url, author, publisher, date, price, rate, comment))


if __name__ == '__main__':
    urls = ['https://book.douban.com/top250?start={0}'.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_info(url)

    file_object.close()


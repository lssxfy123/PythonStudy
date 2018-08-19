# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.8.19
# scrapy爬虫练习
from scrapy import cmdline
cmdline.execute('scrapy crawl books -o books.csv'.split())

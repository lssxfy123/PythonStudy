# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.8.18
# python中执行cmd
from scrapy import cmdline
cmdline.execute('scrapy crawl huxiu -o items.json'.split())

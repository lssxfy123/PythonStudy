# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.24
# 获取代理存储到Redis
from crawler import Crawler
from db import RedisClient
from setting import *
import sys


class Getter:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)


if __name__ == '__main__':
    getter = Getter()
    getter.run()

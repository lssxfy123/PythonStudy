# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.9
# 代理获取模块
from lxml import etree
from utils import get_page
import time


# 元类
class ProxyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            # 如果以包含crawl_，就
            # 认为是爬虫函数
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Crawler(metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{0}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        start_url = 'http://www.66ip.cn/{0}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                selector = etree.HTML(html)
                trs = selector.xpath('.//div[@id="main"]/div[1]/div[1]/table/tr')
                for i in range(1, len(trs)):
                    ip = trs[i].xpath('.//td[1]/text()')[0]
                    port = trs[i].xpath('.//td[2]/text()')[0]
                    yield ':'.join([ip, port])

    def crawl_ip3366(self, page_count=4):
        start_url = 'http://www.ip3366.net/free/?stype=1&page={0}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                selector = etree.HTML(html)
                table = selector.xpath('.//div[@id="list"]/table')[0]
                trs = table.xpath('.//tr')
                for i in range(1, len(trs)):
                    ip = trs[i].xpath('.//td[1]/text()')[0]
                    port = trs[i].xpath('.//td[2]/text()')[0]
                    yield ':'.join([ip, port])

    def crawl_kuaidaili(self, page_count=4):
        start_url = 'http://www.kuaidaili.com/free/inha/{0}/'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                selector = etree.HTML(html)
                table = selector.xpath('.//div[@id="list"]/table')[0]
                trs = table.xpath('.//tr')
                for i in range(1, len(trs)):
                    ip = trs[i].xpath('.//td[1]/text()')[0]
                    port = trs[i].xpath('.//td[2]/text()')[0]
                    yield ':'.join([ip, port])
            time.sleep(1)

    def crawl_xicidaili(self, page_count=4):
        start_url = 'http://www.xicidaili.com/nn/{0}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                selector = etree.HTML(html)
                trs = selector.xpath('.//table[@id="ip_list"]/tr')
                for i in range(1, len(trs)):
                    ip = trs[i].xpath('.//td[2]/text()')[0]
                    port = trs[i].xpath('.//td[3]/text()')[0]
                    yield ':'.join([ip, port])


if __name__ == '__main__':
    crawler = Crawler()

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.28
# scrapy爬取简书-热门专题
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from zhuanti.items import ZhuantiItem


class Zhuanti(CrawlSpider):
    name = 'zhuanti'
    start_urls = ['http://www.jianshu.com/recommendations/collections?page=1&order_by=hot']

    def parse(self, response):
        item = ZhuantiItem()
        selector = Selector(response)
        infos = selector.xpath('//div[@class="col-xs-8"]')
        for info in infos:
            try:
                name = info.xpath('div/a/h4/text()').extract()[0]
                content = info.xpath('div/a/p/text()').extract()[0]
                article = info.xpath('div/div/a/text()').extract()[0]
                fans = info.xpath('div/div/text()').extract()[0]

                item['name'] = name
                item['content'] = content
                item['article'] = article
                item['fans'] = fans
                yield item  # 返回数据
            except IndexError:
                pass

        urls = ['http://www.jianshu.com/recommendations/collections?page={0}' \
                '&order_by=hot'.format(str(i)) for i in range(2, 11)]
        for url in urls:
            yield Request(url, callback=self.parse)


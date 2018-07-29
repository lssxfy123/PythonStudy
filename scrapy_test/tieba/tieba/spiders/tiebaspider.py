# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.28
# scrapy爬取知乎
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from tieba.items import TiebaItem


class tieba(CrawlSpider):
    name = 'tieba'
    start_urls = ['https://www.zhihu.com/topic/19552832/top-answers?page=1']

    def parse(self, response):
        item = TiebaItem()
        selector = Selector(response)
        infos = selector.xpath('//div[@class="List-item TopicFeedItem"]')
        for info in infos:
            try:
                question = info.xpath('div/h2/div/a/text()').extract()[0].strip()
                content = info.xpath('.//div[@class="RichContent-inner"]/span/text()').extract()[0].strip()
                item['question'] = question
                item['content'] = content
                yield item
            except IndexError:
                pass

        urls = ['https://www.zhihu.com/topic/19552832/top-answers?page={0}'.format(str(i)) for i in range(2, 3)]
        for url in urls:
            yield Request(url, callback=self.parse)

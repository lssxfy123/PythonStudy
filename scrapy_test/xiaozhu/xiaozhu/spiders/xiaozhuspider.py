# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.28
# scrapy框架测试
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from xiaozhu.items import XiaozhuItem


class XiaoZhu(CrawlSpider):
    name = 'xiaozhu'
    start_urls = ['http://bj.xiaozhu.com/fangzi/6937392816.html']

    def parse(self, response):
        item = XiaozhuItem()
        selector = Selector(response)
        title = selector.xpath('//h4/em/text()').extract()[0]
        address = selector.xpath('//p/span[@class="pr5"]/text()').extract()[0].strip()
        price = selector.xpath('//*[@id="pricePart"]/div[1]/span/text()').extract()[0]
        lease_type = selector.xpath('//*[@id="introduce"]/li[1]/h6/text()').extract()[0]
        suggestion = selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]
        bed = selector.xpath('//*[@id="introduce"]/li[3]/h6/text()').extract()[0]

        item['title'] = title
        item['address'] = address
        item['price'] = price
        item['lease_type'] = lease_type
        item['suggestion'] = suggestion
        item['bed'] = bed

        yield item

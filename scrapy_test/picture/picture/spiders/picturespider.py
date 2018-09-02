# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
from scrapy.http import Request
from picture.items import PictureItem
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader


class PicturespiderSpider(scrapy.Spider):
    name = 'picturespider'
    allowed_domains = ['web']
    start_urls = ['http://t66y.com/thread0806.php?fid=16&search=&page={0}'.format(i) for i in range(1, 3)]

    def __init__(self):
        self.http_header = "http://t66y.com/"

    def parse(self, response):
        regex = re.compile(r'\[\d+P\]$')
        selector = Selector(response)
        trs = selector.xpath('.//tr[@class="tr3 t_one tac"]')
        for tr in trs:
            try:
                link = tr.xpath('.//h3/a')
                href = link.xpath('.//@href').extract()[0]
                title = link.xpath('text()').extract()
                if len(title) > 0:
                    title = title[0]
                else:
                    title = link.xpath('.//*/text()').extract()[0]
                if regex.search(title):
                    request = Request(self.http_header + href, callback=lambda response, tag=title: self.parse_item(response, tag), dont_filter=True)
                    yield request
            except:
                pass

    def parse_item(self, response, tag):
        item = PictureItem()
        selector = Selector(response)
        pictures = selector.xpath('//input[@type="image"]/@data-src').extract()[1:]
        item['image_urls'] = pictures
        item['title'] = tag
        yield item

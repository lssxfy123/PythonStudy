# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.8.19
# scrapy爬虫练习
from books.items import BooksItem
from scrapy import Request, Spider, Selector


class BooksSpider(Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        selector = Selector(response)
        book_infos = selector.xpath('.//section/div[2]/ol/li/article[@class="product_pod"]')
        for book_info in book_infos:
            item = BooksItem()
            item['title'] = book_info.xpath('h3/a/@title').extract()[0]
            item['price'] = book_info.xpath('div/p/text()').extract()[0]
            yield item

        next_page = selector.xpath('.//section/div[2]/div/ul/li[@class="next"]')
        if next_page:
            url = next_page.xpath('a/@href').extract()[0]
            url = response.urljoin(url)  # 构建绝对url路径
            yield Request(url, callback=self.parse)

from coolscrapy.items import HuxiuItem
from scrapy import Request, Spider


class HuxiuSpider(Spider):
    name = 'huxiu'
    start_urls = ["http://www.huxiu.com/index.php"]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt index-article-list-yh"]'):
            url = response.urljoin(sel.xpath('h2/a/@href').extract()[0])
            yield Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('.//div[@class="article-wrap"]')
        item = HuxiuItem()
        item['title'] = detail.xpath('h1/text()').extract()[0]
        item['link'] = response.url
        yield item


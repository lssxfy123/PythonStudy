from huangye.items import HuangyeItem
from scrapy import Request, Selector, Spider


class HuangyeSpider(Spider):
    name = 'Huangye'
    start_urls = ["http://b2b.huangye88.com/gongsi/"]

    def parse(self, response):
        selector = Selector(response)
        company_list = selector.xpath('.//ul[@class="cats_list2"]/li/a/@href').extract()
        for company_url in company_list:
            company_url += "company_contact.html"
            yield Request(company_url, callback=self.parse_url)

    def parse_url(self, response):
        selector = Selector(response)
        item = HuangyeItem()
        name = selector.xpath('.//ul[@class="con-txt"]/li[1]/text()').extract()
        phone = selector.xpath('.//ul[@class="con-txt"]/li[2]/text()').extract()
        print(name)
        print(phone)
        item["name"] = name
        item["phone"] = phone
        return item

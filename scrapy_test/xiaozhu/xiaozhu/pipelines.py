# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaozhuPipeline(object):
    def process_item(self, item, spider):
        with open('xiaozhu.txt', 'a+') as fp:
            fp.write(item['title'] + '\n')
            fp.write(item['address'] + '\n')
            fp.write(item['price'] + '\n')
            fp.write(item['lease_type'] + '\n')
            fp.write(item['suggestion'] + '\n')
            fp.write(item['bed'] + '\n')
        return item

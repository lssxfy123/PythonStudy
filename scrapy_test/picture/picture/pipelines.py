# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import os
import requests
from picture.settings import IMAGES_STORE

class PicturePipeline(object):
    def process_item(self, item, spider):
        file_path = IMAGES_STORE + re.sub('[\/:*?"<>|]', '', item["title"].strip())
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        image_urls = item['image_urls']
        for url in image_urls:
            html = requests.get(url)
            file_name = file_path + '/' + url.split(r'/')[-1]
            with open(file_name, 'wb') as file_obj:
                file_obj.write(html.content)
        return item

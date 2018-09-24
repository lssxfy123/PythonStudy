# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.29
# 爬取图片：根据时间筛选
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import requests
import time
import datetime
import re
import os
from multiprocessing import Pool


class CrawlerPictures:
    def __init__(self, total_url):
        self.total_url = total_url
        self.max_page_number = 1
        self.first_layer_urls = []
        self.pictures = []
        self.host_headers = {
            'Host': 'www.mzitu.com',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'text/html; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.mzitu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }

        self.picture_headers = {
            'Referer': 'http://i.meizitu.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }

        self.url_header = 'http://www.mzitu.com/page/'

        self.date_time = datetime.datetime.strptime('2018-08-05', '%Y-%m-%d')

    # 获取第一层所有url
    def get_first_layer_url(self):
        html = requests.get(self.total_url, headers=self.host_headers)
        selector = etree.HTML(html.content)
        pages = selector.xpath('//div[@class="nav-links"]/a[@class="page-numbers"]/text()')
        self.max_page_number = int(pages[-1])
        for i in range(1, self.max_page_number + 1):
            self.first_layer_urls.append(self.url_header + str(i))

    # 获取第二层所有url
    def get_second_layer_url(self):
        for url in self.first_layer_urls:
            html = requests.get(url, headers=self.host_headers)
            if html.status_code == 200:
                selector = etree.HTML(html.content)
                picture_urls = selector.xpath('//div[@class="postlist"]/ul/li')
                for picture_url in picture_urls:
                    picture_time = picture_url.xpath('span[@class="time"]/text()')[0]
                    picture_time = datetime.datetime.strptime(picture_time, '%Y-%m-%d')
                    if picture_time >= self.date_time:
                        picture = PictureUrl(picture_url.xpath('a')[0], self.host_headers)
                        picture.get_image_url()
                        self.pictures.append(picture)
                    else:
                        return

                    time.sleep(1)

    def get_image(self, url, file_path):
        html = requests.get(url, headers=self.host_headers)
        selector = etree.HTML(html.text)
        image_url = selector.xpath('.//div[@class="main-image"]/p/a/img/@src')[0]
        file_name = file_path + '/' + image_url.split(r'/')[-1]
        image_html = requests.get(image_url, headers=self.picture_headers)
        with open(file_name, 'wb') as file_obj:
            file_obj.write(image_html.content)

    def get_images(self):
        print('start get images')
        pool = Pool(processes=4)
        for picture in self.pictures:
            for url in picture.urls:
                pool.apply_async(self.get_image, args=(url, picture.file_path))

        pool.close()
        pool.join()


class PictureUrl:
    def __init__(self, picture_url, host_headers):
        self.title = picture_url.xpath('img/@alt')[0]
        self.save_path = "d:/pictures/"
        self.urls = []
        self.href = picture_url.get('href')
        self.host_headers = host_headers
        file_path = self.save_path + re.sub('[\/:*?"<>|]', '', self.title.strip())

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path

    def get_image_url(self):
        html = requests.get(self.href, headers=self.host_headers)
        girl_selector = etree.HTML(html.text)
        max_image = girl_selector.xpath('.//div[@class="pagenavi"]/a/span/text()')[-2]
        for j in range(1, int(max_image) + 1):
            url = self.href + '/' + str(j)
            self.urls.append(url)


if __name__ == '__main__':
    total_url = "http://www.mzitu.com/"
    crawler_picture = CrawlerPictures(total_url)
    crawler_picture.get_first_layer_url()
    crawler_picture.get_second_layer_url()
    crawler_picture.get_images()

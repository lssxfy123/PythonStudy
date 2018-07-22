# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.22
# 爬取图片
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import requests
import time
import re
import os
import win32api
import win32con
import win32clipboard
from ctypes import *


class CrawlerPictures:
    def __init__(self, total_url):
        self.total_url = total_url
        self.max_page_number = 1
        self.first_layer_urls = []
        self.picture_urls = []
        self.host_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.picture_headers = {
            'Referer': 'http://i.meizitu.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }

        self.url_header = 'https://www.meitulu.com/img.html?img='

    # 获取第一层所有url
    def get_first_layer_url(self):
        html = requests.get(self.total_url, headers=self.host_headers)
        selector = etree.HTML(html.content)
        pages = selector.xpath('//div[@class="boxs"]/ul/li/a')
        for page in pages:
            picture = PictureUrl(page, self.host_headers)
            picture.get_image_url()
            self.first_layer_urls.append(picture)

    # 获取所有图片
    def get_images(self):
        for picture in self.first_layer_urls:
            for url in picture.urls:
                self.get_image(self.url_header + url, picture.file_path)

    def get_image(self, url, file_path):
        suffix = url.split(r'/')[-1]
        file_path = file_path.replace('/', '\\') + '\\' + suffix
        self.driver.get(url)
        self.driver.implicitly_wait(6)
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(file_path)
        win32clipboard.CloseClipboard()

        # 鼠标定位输入框并点击
        windll.user32.SetCursorPos(700, 510)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        time.sleep(1)

        # 按下shift+v
        win32api.keybd_event(0x10, 0, 0, 0)
        win32api.keybd_event(0x56, 0, 0, 0)
        win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x10, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)

        # 按下ctrl+v
        win32api.keybd_event(0x11, 0, 0, 0)
        win32api.keybd_event(0x56, 0, 0, 0)
        win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)

        # 按下回车
        win32api.keybd_event(0x0D, 0, 0, 0)
        win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(2)

    def close(self):
        self.driver.close()


class PictureUrl:
    def __init__(self, picture_url, host_headers):
        self.title = picture_url.xpath('img/@alt')[0]
        self.number = re.findall('\[(\d+)\]', self.title)[0]
        self.save_path = "d:/pictures/"
        self.urls = []
        self.href = picture_url.get('href')
        self.item_number = re.findall('(\d+)', self.href)[0]
        self.host_headers = host_headers
        file_path = self.save_path + re.sub('[\/:*?"<>|]', '', self.title.strip())

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path
        self.header_url = 'https://mtl.ttsqgs.com/images/img/'

    def get_image_url(self):
        for j in range(1, int(self.number) + 1):
            url = self.header_url + self.item_number + '/' + str(j) + '.jpg'
            self.urls.append(url)


if __name__ == '__main__':
    total_url = "https://www.meitulu.com/search/%E9%9B%AA%E7%B3%95"
    crawler_picture = CrawlerPictures(total_url)
    crawler_picture.get_first_layer_url()
    crawler_picture.get_images()
    crawler_picture.close()

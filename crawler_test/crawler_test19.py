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
    def __init__(self, urls_file):
        self.urls_file = urls_file
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
        with open(self.urls_file) as file_lines:
            lines = file_lines.readlines()
            for line in lines:
                picture = PictureUrl(line, self.host_headers)
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
    def __init__(self, url_info, host_headers):
        picture_url = url_info.split(';')[0]
        self.title = re.findall('(\d+)', picture_url)[0]
        # number_text = selector.xpath('.//div[@class="c_l"]/p[last()-3]/text()')[0]
        self.start_number = url_info.split(';')[1].split('-')[0]  # re.findall('(\d+)', number_text)[0]
        self.end_number = url_info.split(';')[1].split('-')[1]
        self.save_path = "d:/pictures/"
        self.urls = []
        self.href = picture_url
        self.is_found = True

        self.item_number = re.findall('(\d+)', self.href)[0]
        self.host_headers = host_headers
        file_path = self.save_path + re.sub('[\/:*?"<>|]', '', self.title.strip())

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path
        self.header_url = 'https://mtl.ttsqgs.com/images/img/'
        # self.proxies = {'http': '118.190.95.35:9001'}
        # html = requests.get(picture_url, headers=host_headers)
        # self.is_found = True
        # if html.status_code == 404:
        #     print('not found')
        #     self.is_found = False
        # else:
        #     selector = etree.HTML(html.content)

    def get_image_url(self):
        if self.is_found:
            for j in range(int(self.start_number), int(self.end_number) + 1):
                url = self.header_url + self.item_number + '/' + str(j) + '.jpg'
                self.urls.append(url)


if __name__ == '__main__':
    crawler_picture = CrawlerPictures('urls.txt')
    crawler_picture.get_first_layer_url()
    crawler_picture.get_images()
    crawler_picture.close()

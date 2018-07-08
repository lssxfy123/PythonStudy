# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.8
# 爬取淘宝网信息
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import time
import pymongo
from mongodb_test import mongo_host
from mongodb_test import mongo_port

client = pymongo.MongoClient(mongo_host, mongo_port)
mydb = client['mydb']
taobao = mydb['taobao']

# 无GUI
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


def get_info(url, page):
    page += 1
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        data = info.xpath('div/div/a')[0]
        goods = data.xpath('string(.)').strip()
        price = info.xpath('div/div/div/strong/text()')[0]
        sell = info.xpath('div/div/div[@class="deal-cnt"]/text()')[0]
        shop = info.xpath('div[2]/div[3]/div[1]/a/span[2]/text()')[0]
        address = info.xpath('div[2]/div[3]/div[2]/text()')[0]
        commodity = {
            'good': goods,
            'price': price,
            'sell': sell,
            'shop': shop,
            'address': address
        }
        taobao.insert_one(commodity)
    if page <= 5:
        next_page(url, page)  # 进入下一页
    else:
        pass


def next_page(url, page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(4)
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    get_info(driver.current_url, page)


if __name__ == '__main__':
    page = 1
    url = 'https://www.taobao.com/'
    driver.get(url)
    driver.implicitly_wait(10)

    # 淘宝网页面搜索框输入的<input>元素id为q
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')

    # 搜索按钮的class='btn-search'
    driver.find_element_by_class_name('btn-search').click()
    get_info(driver.current_url, page)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.14
# 嵌入js脚本
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()

    page = 1
    url = 'https://www.taobao.com/'
    driver.get(url)
    driver.implicitly_wait(10)

    # 淘宝网页面搜索框输入的<input>元素id为q
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')

    # 搜索按钮的class='btn-search'
    # 操作事件时采用对应的click()方法
    # driver.find_element_by_class_name('btn-search').click()

    # 采用嵌入js脚本操作事件
    btn_search = driver.find_element_by_class_name('btn-search')
    driver.execute_script('arguments[0].click();', btn_search)

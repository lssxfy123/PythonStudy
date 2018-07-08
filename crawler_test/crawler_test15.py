# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.7.7
# Selenium模拟浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pymongo
from mongodb_test import mongo_host
from mongodb_test import mongo_port


client = pymongo.MongoClient(mongo_host, mongo_port)
mydb = client['mydb']
qq_shuo = mydb['qq_shuo']

# 带有GUI
driver = webdriver.Chrome()
driver.maximize_window()


def get_info(qq):
    driver.get('https://user.qzone.qq.com/{0}/311'.format(qq))
    driver.implicitly_wait(10)

    # 是否需要登陆
    try:
        driver.find_element_by_id('login_div')
        flag = True
    except:
        flag = False

    # 需要登录
    if flag:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('357455175')  # 账号
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('lss19880124')  # 密码
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
        driver.implicitly_wait(3)

    # 是否可以访问QQ好友空间
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        flag1 = True
    except:
        flag1 = False

    if flag1:
        driver.switch_to.frame('app_canvas_frame')
        contents = driver.find_elements_by_css_selector('.content')
        times = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for content, tim in zip(contents, times):
            data = {
                'time': tim.text,
                'content': content.text
            }
            qq_shuo.insert_one(data)


if __name__ == '__main__':
    get_info('393466863')

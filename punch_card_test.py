#模拟邮箱登录
import time
from splinter import Browser
from selenium import webdriver
from urllib import request

def Splinter(url):
    browser = Browser('chrome')
    browser.visit(url)
    time.sleep(5)
    with browser.get_iframe('x-URS-iframe') as iframe:
        browser.find_by_name('email').fill('liushenshenxfy')
        browser.find_by_name('password').fill('lss19871203')
        browser.find_by_id('dologin').click()
    time.sleep(8)
    browser.quit()

if __name__ == '__main__':
    url = 'http://www.126.com'
    Splinter(url)




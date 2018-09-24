# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.8
# robots协议测试
from urllib.robotparser import RobotFileParser
url = 'http://www.jianshu.com/robots.txt'
rp = RobotFileParser(url)
rp.read()
# 在scrapy中，如果希望爬取robots.txt禁止的页面，需要禁用robots
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))  # False，不允许爬取

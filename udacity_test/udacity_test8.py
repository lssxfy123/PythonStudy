# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.7
# python练习测试8：“我的微信好友”项目测试
import re
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
values = (66, 33, 22)
labels = [u'Negative', u'Neutral', u'Positive']
plt.xlabel(u'Sentiment Analysis')
plt.ylabel(u'Number')
plt.xticks(range(3), labels)
plt.bar(range(3), values)

plt.title('Sentiment Analysis of Friends signature')
plt.show()

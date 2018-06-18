# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.17
# Lxml库测试
import lxml
from lxml import etree

# 其中第2个<li>缺少了结束符
# lxml会自动补全
text = """
<div>
<ul>
<li class="red"><h1>red flowers</h1></li>
<li class="blue"><h5>blue flowers</h5>
</ul>
</div>
"""
html = lxml.etree.HTML(text)
result = etree.tostring(html)
print(result)

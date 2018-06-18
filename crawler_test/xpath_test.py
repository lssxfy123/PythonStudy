# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.17
# xpath测试
from lxml import etree

if __name__ == '__main__':
    text = """
    <td>
        <div>
            <span>aa</span>
            <span>bb</span>
        </div>
        <div>
            <span>cc</span>
        </div>
    </td>"""

    selector = etree.HTML(text)
    # 获取父元素为div，祖父元素为td的所有span元素
    result = selector.xpath('//td/div/span')
    print(result)  # 有3个span元素
    for span in result:
        print(span.text)

    # 获取父元素为div，祖父元素为td的第1个span元素
    # 从结果中可以看出，属于不同的div的第1个span元素
    # 都会被查询到
    result = selector.xpath('//td/div/span[1]')
    print(result)  # 有两个span元素
    for span in result:
        print(span.text)

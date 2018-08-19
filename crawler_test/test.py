from lxml import etree
import requests

# url = "http://www.sxotu.com/u/20180729/17065477.jpg"
#
# file_name = "d:/pictures/1.jpg"
#
# html = requests.get(url)
#
# if html.status_code == 200:
#     print('can crawler')
#     with open(file_name, 'wb') as file_obj:
#         file_obj.write(html.content)
# else:
#     print('not crawler')


url = "http://t66y.com/htm_data/16/1808/3226898.html"
html = requests.get(url)
if html.status_code == 200:
    print('can crawler')
    selector = etree.HTML(html.content)
    pictures = selector.xpath('//input[@type="image"]')
    pictures1 = pictures[1:]
    for picture in pictures1:
        print(picture)
else:
    print('not crawler')

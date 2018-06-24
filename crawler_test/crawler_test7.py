# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.23
# API调用
# 百度地图API
import requests
import json
import pprint

if __name__ == '__main__':
    address = input('请输入地点：')
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    url = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(url, par)
    json_data = json.loads(res.text)
    pprint.pprint(json_data)

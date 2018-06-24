# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.23
# json
import json

if __name__ == '__main__':
    json_str = '{"user_man":[{"name":"Peter"},{"name":"xiaoming"}],"user_woman":[{"name":"Anni"},{"name":"zhangsan"}]}'
    json_data = json.loads(json_str)
    print(json_data.get("user_man"))
    print(json_data.get("user_man")[0].get("name"))

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.6.234
# MongoDB测试
import pymongo

mongo_host = 'localhost'
mongo_port = 27017

if __name__ == '__main__':
    client = pymongo.MongoClient(mongo_host, mongo_port)
    mydb = client['mydb']  # 如果没有就创建mydb数据库
    test = mydb['test']  # 如果没有就创建test数据集合
    test.insert_one({'name': 'Jan', 'sex': '男', 'grade': 89})

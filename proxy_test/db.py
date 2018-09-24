# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.9
# 代理存储模块
import redis
from error import PoolEmptyError
from setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re


class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    # 添加代理
    def add(self, proxy, score=INITIAL_SCORE):
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    # 获取随机代理
    def random(self):
        # 获取最高分代理范围
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            # 代理按分数排序
            result = self.db.zrevrange(REDIS_KEY, MIN_SCORE, MAX_SCORE)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    # 代理减分
    def decrease(self, proxy):
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)
    
    # 判断是否存在
    def exists(self, proxy):
        return not self.db.zscore(REDIS_KEY, proxy)
    
    # 将代理设置为MAX_SCORE
    def max(self, proxy):
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    # 获取数量
    def count(self):
        return self.db.zcard(REDIS_KEY)

    # 获取全部代理
    def all(self):
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

    # 批量获取
    def batch(self, start, stop):
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)



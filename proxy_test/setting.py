# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.9
# 代理池设置

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

# 代理池数量限制
POOL_UPPER_THRESHOLD = 10000

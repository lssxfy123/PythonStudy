# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.25
# map：序列中映射函数
counters = [1, 2, 3, 4]


def inc(x): return x + 10


# map将counters每一个元素分别调用inc()
print(list(map(inc, counters)))  # [11, 12, 13, 14]
print(list(map((lambda x: x + 10), counters)))  # [11, 12, 13, 14]

# map可以将N个参数的函数用于N个序列
# 如果序列的长度不一致，则按最短序列匹配
# 1 ** 2, 2 ** 3, 3 ** 4
print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))  # [1, 8, 81]
print(list(map(pow, [1, 2, 3, 4], [2, 3, 4])))  # [1, 8, 81]

# filter过滤
print(list(filter((lambda x: x > 0), range(-5, 5))))  # [1, 2, 3, 4]

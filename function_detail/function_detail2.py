# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 多态


def times(x, y):
    return x * y


print(times(2, 4))  # 8
print(times('Ni', 4))  # NiNiNiNi


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


s1 = 'SPAM'
s2 = 'SCAM'
print(intersect(s1, s2))

# 列表中对象的类型有可能不相同
list1 = [1, 2, 3, 'a']
list2 = (1, 'a')
print(intersect(list1, list2))

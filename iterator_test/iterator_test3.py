# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.22
# range, map, zip与字典迭代器
# range
R = range(10)
it1 = iter(R)  # range不是自身的迭代器，需要使用iter函数
print(next(it1))  # 0
print(next(it1))  # 1

# map
M = map(abs, (-3, -2, -1))
print(next(M))  # 3，map是自身的迭代器
print(next(M))  # 2
print(next(M))  # 1

Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))  # (1, 10)，zip是自身的迭代器
print(next(Z))  # (2, 20)

# 多个迭代器 VS 单个迭代器
# range支持多个迭代器
# iter()返回一个新的对象
R1 = range(1, 10)
print(id(R1))  # 2556288144704
print(id(iter(R1)))  # 2556255252176

# map, zip, filter等支持单个迭代器
# iter()返回自身
M1 = map(abs, (-3, -2, -1))
print(id(M1))  # 2556288879528
print(id(iter(M1)))  # 2556288879528

# 同一个range的两个迭代器互不影响
itr1 = iter(R1)
itr2 = iter(R1)
print(next(itr1))  # 1
print(next(itr2))  # 1

# 同一个map的两个迭代器迭代同一个对象
itm1 = iter(M1)
itm2 = iter(M1)
print(next(itm1))  # 3
print(next(itm2))  # 2
print()

# 字典迭代器
D = dict(a=1, b=2, c=3)
print(D)  # {'a': 1, 'b': 2, 'c': 3}

# dict的keys()不是列表，可迭代
K = D.keys()
print(type(K))  # <class 'dict_keys'>

itk = iter(K)
print(next(itk))  # a
print(next(itk))  # b

# dict的values()不是列表，可迭代
V = D.values()
itv = iter(V)
print(next(itv))  # 1
print(next(itv))  # 2

# 字典本身的迭代器返回key
itd = iter(D)
print(next(itd))  # a

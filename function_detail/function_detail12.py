# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.26
# 生成器表达式
# 将列表解析的[]换成()就是生成器表达式
list_parse = [x ** 2 for x in range(4)]  # 列表解析
gen = (x ** 2 for x in range(4))

# 列表解析会一次将结果都存入内存
print(list_parse)  # [0, 1, 4, 9]
print(gen)  # <generator object <genexpr> at 0x000000EDB4C4F9E8>
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print()

# 生成器是单迭代器
# 使用多个迭代器迭代生成器，
# 会指向同一个对象
G = (c * 4 for c in 'spam')
print(iter(G) is G)  # True
print()
it1 = iter(G)
it2 = iter(G)
print(next(it1))  # ssss
print(next(it1))  # pppp
print(next(it2))  # aaaa
print(next(it2))  # mmmm
# print(next(it2))  # StopIteration

#排序算法
L = [36, 5, -12, 9, -21]
print("[36, 5, -12, 9, -21]由小到大排列", sorted(L))

print("[36, 5, -12, 9, -21]由大到小排列", sorted(L, reverse=True))

#sorted可以接收一个key函数来进行排序
print("[36, 5, -12, 9, -21]按绝对值大小排序", sorted(L, key=abs))

L1 = ['bob', 'about', 'Zoo', 'Credit']
print('忽略大小写的排序', sorted(L1, key = str.lower))
print(L1)

from operator import itemgetter

L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print('按名称排序', sorted(L2, key = itemgetter(0)))
print('按分数排序', sorted(L2, key = lambda t : t[1]))
print('按分数降序排列', sorted(L2, key = itemgetter(1), reverse = True))

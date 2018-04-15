# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.13
# 集合
empty_set = set()  # 空集合
x = set('spaam')
y = {'h', 'a', 'm'}

# 集合是无序，是不可变对象的集合
# 集合本身是可变对象
# 集合会自动删除重复的元素
print(x)
print(y)
print()
print(x & y)
print(x | y)
print(x - y)
print()

# 集合解析
s = {x ** 2 for x in [1, 2, 3, 4]}
print(s)

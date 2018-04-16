# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.16
# 引用 & 拷贝
x = [1, 2, 3]
l = ['a', x, 'b']
d = {'x': x, 'y': 2}
print('original: ')
print(x)
print(l)
print(d)
print()
x[1] = 'surprise'

# 列表和字典存储的都是对象的引用
# 修改x后，l和d会跟着变化
print('modify x: ')
print(x)
print(l)
print(d)
print()

# 如果希望避免上述情况发生，就需要使用拷贝


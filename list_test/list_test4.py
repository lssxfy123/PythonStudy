# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.12
# 列表序列化操作
l1 = [1, 2, 3]
print(l1 + ['a', 'b'])  # [1, 2, 3, 'a', 'b']
print(l1)  # [1, 2, 3]
l1 += ['a', 'b']  # l1 = l1 + ['a', 'b']
print(l1)
print()

# 列表中可以包含不同类型的元素
# 但部分列表方法就无法使用了
# print(l1.sort())  # Error

# 列表嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # [1, 2, 3]

# 列表解析
print([value for value in matrix])
print()
# print(value)  # Error，value未定义
col2 = [row[1] for row in matrix]
print(col2)  # [2, 5, 8]
print([row[1] for row in matrix if row[1] % 2 == 0])  # [2, 8]
print([matrix[i][i] for i in [0, 1, 2]])  # [1, 5, 9]

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Create Date: 2018.3.28
# 操作列表

# for循环操作列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print("great trick")
print("Thank you everyone\n")

# 数值
for value in range(1, 6):
    print(value)
print()

# 数值列表
numbers = list(range(1, 6))
print(numbers)
print()

# 步长为2
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print()

# 空列表
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print("max:")
print(max(squares))
print("min:")
print(min(squares))
print()

big_numbers = list(range(1, 1000000))
sums = sum(big_numbers)
print(sums)

# 列表解析
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

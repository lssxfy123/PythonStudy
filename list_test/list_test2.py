# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Create Date: 2018.3.28
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("1-2:")
print(players[0:2])
print("2-3:")
print(players[1:3])
print("1-4:")
print(players[:4])
print("3-末尾:")
print(players[2:])
print()

# 列表复制
foods = ['pizza', 'falafel', 'carrot']

# 采用切片方式复制列表
# foods与fri_foods是不同的列表
fri_foods = foods[:]

foods.append('cannoli')
fri_foods.append('ice cream')

print("my foods:")
print(foods)
print("\nfriend foods:")
print(fri_foods)
print()

# 如果简单的赋值
foods1 = ['pizza', 'falafel', 'carrot']
fri_foods1 = foods1

foods1.append('cannoli')
fri_foods1.append('ice cream')
print("my foods:")
print(foods1)
print("\nfriend foods:")
print(fri_foods1)
print()

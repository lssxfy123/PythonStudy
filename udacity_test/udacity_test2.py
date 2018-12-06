# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.6
# python练习测试2:zip, enumerate和列表解析
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

print(points)

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))  # replace with your code
print(cast)

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names)
print(heights)

# 矩阵转置
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))   # replace with your code
print(data_transpose)

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for index, item in enumerate(cast):
    cast[index] = item + " " + str(heights[index])

print(cast)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name in scores.keys() if scores[name] >= 65]
print(passed)

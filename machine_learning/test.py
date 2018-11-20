from sklearn import svm
import json
import codecs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# 加载数据集
train_filename = 'train.json'
train_content = pd.read_json(codecs.open(train_filename, mode='r', encoding='utf-8'))

test_filename = 'test.json'
test_content = pd.read_json(codecs.open(test_filename, mode='r', encoding='utf-8'))

# 打印加载的数据集数量
print("菜名数据集一共包含 {} 训练数据 和 {} 测试样例。\n".format(len(train_content), len(test_content)))
if len(train_content) == 39774 and len(test_content) == 9944:
    print("数据成功载入！")
else:
    print("数据载入有问题，请检查文件路径！")


# 创建数组
train_ingredients = train_content['ingredients']
train_targets = train_content['cuisine']

categories=np.unique(train_targets)
# print("一共包含 {} 种菜品，分别是:\n{}".format(len(categories), categories))
# print(train_ingredients)
sum_ingredients = {}
italian_ingredients = {}
ingredients = np.array(train_ingredients)
targets = np.array(train_targets)
# print(ingredients)

for i in np.arange(ingredients.size):
    ingredient = ingredients[i]
    for j in np.arange(len(ingredient)):
        key = ingredients[i][j]
        if sum_ingredients.__contains__(key):
            sum_ingredients[key] += 1
        else:
            sum_ingredients[key] = 1
        if targets[i] == 'italian':
            if italian_ingredients.__contains__(key):
                italian_ingredients[key] += 1
            else:
                italian_ingredients[key] = 1

# print(sum_ingredients)
# print(italian_ingredients)

bags_of_words = list()
for recipe in ingredients:
    tmp = Counter(recipe)
    bags_of_words.append(tmp)

# print(bags_of_words[0])
bags = Counter()
# 数据量太大，Counter中的字典太长
# for bag in bags_of_words:
#     bags += bag
# # bags = bags_of_words[0] + bags_of_words[1] + bags_of_words[2] + bags_of_words[3]
# # bags = sum(bags_of_words[0], Counter())
# print(bags)

# keys = list(tmp.keys())
# values = list(tmp.values())
# for i in range(10):
#     max_value = max(values)
#     max_index = values.index(max_value)
#     sum_ingredients[keys[max_index]] = max_value
#     del values[max_index]
#     del keys[max_index]

targets = np.array(train_targets)


# print(sum_ingredients)

# print(ingredients.shape)
# print(ingredients.dtype)
# print(len(ingredients[0]))



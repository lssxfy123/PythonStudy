# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.7
# 列表形参


def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + "!"
        print(msg)


user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)
print()


# 在函数中修改列表
# 参考function_test4.py
def print_models(unprinted_models, completed_models):
    """模拟打印每个模型，然后
    将其移到另一个列表中
    """
    while unprinted_models:
        current_design = unprinted_models.pop()
        print("Printing models: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)


unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)
print()
print("unprinted_design length: " + str(len(unprinted_design)))


# 禁止修改列表
def show_animals(animals):
    while animals:
        animal = animals.pop()
        print(animal)


animals = ['cat', 'dog']

# 传递列表的副本，其与animals
# 引用不同的对象
show_animals(animals[:])
print()

# animals没有在函数中清空
print(animals)

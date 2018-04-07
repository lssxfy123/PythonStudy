# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.3
# 函数的参数
# 位置参数，基于实参的顺序


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 带有关键字的位置实参，传递给函数key-value对
# 如果使用了关键字实参，则需要放置在所有的位置参数之后
# 关键字实参不允许重复，但顺序可以随意
# describe_pet(animal_type='cat', 'Tom')  # Error
# describe_pet(pet_name='cat', pet_name='Tom')  # Error
describe_pet(animal_type='cat', pet_name='Tom')
describe_pet(pet_name='Mickey', animal_type='mouse')

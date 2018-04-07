# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.4
# 默认值


# 默认值参数也放在非默认参数之后
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)


describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='cat', pet_name='Tom')
print()


def add_end(animals=[]):
    animals.append('End')
    return animals


print(add_end(['dog']))
print()
print(add_end(['cat']))
print()
print(add_end())
print(add_end())


# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.3.30
# if语句
age = 12
if age < 4:
    print("cost is 0")
elif age < 18:
    print("cost is 5")
else:
    print('cost is 10')

alien_color = 'green'
if alien_color == 'green':
    print('Get 5 score')
elif alien_color == 'red':
    print('Get 10 score')
else:
    print('Get 15 score')

# 处理列表数据
toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in toppings:
    if topping == 'green peppers':
        print('Sorry, no green peppers')
    else:
        print('Adding ' + topping)
print()

# 确定列表不为空
toppings = []
if toppings:
    print('Finished making your pizza')
else:
    print("Are you sure you want a plain pizza?")

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.2
# 字典：key-value
# 字典中元素的顺序是未知的
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

# 使用get方法可以有效避免键不存在的异常
# get方法对于不存在的键会返回None
print(alien_0.get('color'))  # green
print(alien_0.get('color1'))  # None
# print(alien_0['color1'])  # KeyError异常
print()

# 键的唯一性
alien_1 = {'color': 'green', 'points': 5, 'color': 'red'}

# 输出为：{'color': 'red', 'points': 5}
print(alien_1)

# 添加key-value
# 类似C++中的map
# 如果key不存在就添加
# 如果key存在就修改其值
alien_1['x_position'] = 0
alien_1['y_position'] = 25
alien_1['points'] = 6
print(alien_1)
print()

# 判断键是否存在
print(alien_0.__contains__('color'))
print()

# 使用字典时，通常先创建一个空字典
alien_2 = {}
alien_2['x_position'] = 0
alien_2['y_position'] = 25
alien_2['speed'] = 'medium'

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment
print('new x_position:' + str(alien_2['x_position']))
print()

# 删除key-value
del alien_2['speed']
alien_2.pop('x_position')
print(alien_2)
print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'ruby'
}

print(favorite_languages)

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.2
# 嵌套

# 列表中存储字典
aliens = []

# 创建多个元素
for number in range(0, 10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 批量修改
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[0:5]:
    print(alien)
print()

# 字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("You ordered a " + pizza['crust'] + ' with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)
print()

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print('full name: ' + full_name.title())
    print('location: ' + location)

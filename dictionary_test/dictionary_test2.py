# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.2
# 遍历字典
users = {
   'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# 遍历所有key-value
for key, value in users.items():
    print('\nKey: ' + key)
    print('value: ' + value)

# 遍历所有的keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'ruby',
    'jam': 'python'
}

for name in favorite_languages.keys():
    print(name)
print()

# 遍历所有的values
for language in favorite_languages.values():
    print(language)
print()

# 提取独一无二的value
for language1 in set(favorite_languages.values()):
    print(language1)

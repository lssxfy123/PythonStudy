# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.3
# while循环处理列表和字典

# 在for循环中不应修改列表
# 例如增加或删除元素等操作
# 在while循环中可以
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('The following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 循环删除元素
print()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
print()
while 'cat' in pets:
    pets.remove('cat')
print(pets)

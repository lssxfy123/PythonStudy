# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.7
# 任意数量的关键字实参


# 关键字参数user_info要放在最后
# 程序自动将user_info封装成字典
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


# 以下两种调用等效
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
user_profile = build_profile(first='albert', last='einstein', location='princeton', field='physics')
print(user_profile)
print()


# 命名关键字实参
# 使用*运算符，只接收city和job关键字实参
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
# person('Tom', 23)  # 缺少2个关键字参数
# person('Tom', 23, addr='Beijing', code='123')  # 关键字不匹配

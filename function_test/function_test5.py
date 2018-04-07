# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.7
# 函数返回值


def get_format_name(first_name, last_name):
    """返回整洁的名字"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_format_name('jimi', 'hendrix')
print(musician)
print()


# 返回字典
def build_person(first_name, last_name):
    """返回一个字典"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
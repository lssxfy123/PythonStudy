# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.3
# 函数


def greet_user():
    """显示简单的问候语"""
    print('Hello!')


greet_user()


def greet_user(username):
    """显示简单的问候语"""
    print('Hello! ' + str(username).title())


greet_user('Jame')


# 空函数，什么都不干
def pop():
    pass


# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.26
# 函数装饰器


class Spam:
    number_count = 0

    def __init__(self):
        Spam.number_count += 1

    # 函数装饰器定义静态方法
    @staticmethod
    def print_number_count():
        print('Number of instances created: ', Spam.number_count)


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.print_number_count()

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.8
# __del__


class Life:
    def __init__(self, name='unknown'):
        print('Hello', name)
        self.name = name

    def __del__(self):
        print('Goodbye', self.name)


brain = Life('Brain')
brain = 1  # 失去Life的最后一实例，触发__del__函数

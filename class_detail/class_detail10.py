# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.7
# __contains__和__getitem__


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):  # 索引，切片
        print('get[{0}]:'.format(i), end='')

    # 优先级高于__getitem__
    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    # 优先级高于__iter__
    def __contains__(self, x):  # in
        print('contains: ', end='')
        return x in self.data


if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)  # 调用__contains__, contains: True
    for i in X:  # 先执行__iter__，然后__next__
        print(i, end=' | ')

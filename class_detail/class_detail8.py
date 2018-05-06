# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 自定义迭代器


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):  # 自定义迭代器
        return self  # 返回实例本身，支持单个迭代器

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == '__main__':
    for i in Squares(1, 5):
        print(i, end=' ')
    print()

    X = Squares(1, 5)
    it1 = iter(X)
    it2 = iter(X)
    print(next(it1))  # 1
    print(next(it2))  # 4
    print(next(it1))  # 9

# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 自定义多个迭代器


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):  # 支持多个迭代
        return SkipIterator(self.wrapped)


if __name__ == '__main__':
    alpha = 'abcedf'
    skipper = SkipObject(alpha)
    it1 = iter(skipper)
    it2 = iter(skipper)
    print(next(it1))  # a
    print(next(it2))  # a
    print(next(it1))  # b
    print(next(it2))  # b

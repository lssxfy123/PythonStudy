# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.9
# 扩展内置类型


# 扩展内置类型list
class MyList(list):
    def __getitem__(self, item):
        print('indexing {0} at {1}'.format(self, item))
        return list.__getitem__(self, item - 1)


if __name__ == '__main__':
    x = MyList('abcd')
    print(x)
    print(x[1])
    print(x[3])
    print()
    x.append('spam')
    print(x)
    x.reverse()
    print(x)

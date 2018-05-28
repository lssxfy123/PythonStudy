# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.27
# 私有属性-装饰器
trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


def private(*privates):
    def decorator(class_name):
        class Instance:
            def __init__(self, *args, **kwargs):
                self.wrapped = class_name(*args, **kwargs)

            # __getattr__和__setattr__重载“点号”运算符
            # 无论是调用方法还是属性都会触发
            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return Instance
    return decorator


if __name__ == '__main__':
    trace_me = True

    # Doubler = private('data', 'size')(Doubler)
    @private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('{0} => {1}'.format(self.label, self.data))

    x = Doubler('x is', [1, 2, 3])
    print(x.label)
    x.display()
    print()
    x.double()
    x.display()
    x.label = 'spam'
    # print(x.size())  # raise TypeError
    # print(x.data)  # raise TypeError

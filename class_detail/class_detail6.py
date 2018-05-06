# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.6
# 类接口技术


class Super:
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined!'


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        super().method()
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

    y = Super()
    # y.delegate()  # AssertionError: action must be defined!

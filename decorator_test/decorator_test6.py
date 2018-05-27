# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.27
# 私有属性-简单的实现


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value


class Test(Privacy):
    privates = ['age', 'name']  # 类的属性


if __name__ == '__main__':
    x = Test()
    # x.name = 'Bob'  # 抛出异常
    # x.age = 20  # 抛出异常

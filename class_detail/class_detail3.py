# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.5
# 类的继承
import class_detail2


# 类是模块内的属性
class SecondClass(class_detail2.FirstClass):
    def display(self):  # 重写了超类的方法
        print('Current value = {0}'.format(self.data))


class ThreeClass(class_detail2.FirstClass):
    def display(self, name):  # 构成重载
        print("value is {0} and {1}".format(self.data, name))


if __name__ == '__main__':
    z = SecondClass()
    z.set_data(42)
    z.display()

    s = ThreeClass()
    s.set_data(53)
    # s.display()  # Error
    s.display("dog")

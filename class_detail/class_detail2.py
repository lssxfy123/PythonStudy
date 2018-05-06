# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.5
# 类


class FirstClass:
    count = 0  # 类的属性

    def __init__(self):
        self.__name = "First"

    def set_data(self, value):
        self.data = value  # 每个实例对象都有data属性

    def display(self):
        print(self.data)


if __name__ == '__main__':
    x = FirstClass()
    FirstClass.count += 1
    y = FirstClass()
    FirstClass.count += 1

    x.set_data("King Arthur")
    y.set_data(3.14159)

    x.display()
    y.display()
    print(FirstClass.count)

    x.data = "New value"  # ok，可以直接访问实例属性
    x.display()
    # print(x.__name)  # Error，无法访问__name

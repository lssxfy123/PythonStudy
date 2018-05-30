# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.30
# 描述符使用的状态


# 使用描述符实例的状态
class DescriptorState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescriptorState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('DescriptorState set')
        self.value = value


# 使用客户类实例的状态
class InstanceState:
    def __get__(self, instance, owner):
        print('InstanceState get')
        return instance._x * 100

    def __set__(self, instance, value):
        print('InstanceState set')
        instance._x = value


class CalcAttrs:
    attr1 = DescriptorState(2)
    attr2 = InstanceState()

    def __init__(self):
        self._x = 3


if __name__ == '__main__':
    obj = CalcAttrs()
    print(obj.attr1)
    print(obj.attr2)
    print()
    obj.attr1 = 5
    obj.attr2 = 6
    print(obj.attr1)
    print(obj.attr2)

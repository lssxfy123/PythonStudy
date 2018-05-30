# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.30
# 描述符


# 描述符类
# 带有__get__, __set__, __delete__
# 都可以看做描述符类
class Name:
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name
    name = Name()  # 描述符实例赋给类属性（必须是类属性）


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    # Person.name  # AttributeError，name属性会访问到实例属性_name

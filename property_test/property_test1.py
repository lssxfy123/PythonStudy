# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.27
# 属性管理


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('fetch...')
        return self._name

    def set_name(self, value):
        print('change...')
        self._name = value

    def del_name(self):
        print('remove...')
        del self._name
    name = property(get_name, set_name, del_name, "name property docs")


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    # print(bob.name)  # AttributeError

    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Person.name.__doc__)

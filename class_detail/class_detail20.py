# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.9.23
# 元类-ORM映射


class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '{0}:{1}'.format(self.name, self.column_type)


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


# 元类
# 排除对Model类的修改(其为所有表的基类)
# 在Model子类中查找定义的类的所有属性，如果为Field，
# 保存到dict中，并将字典存储到__mappings__属性，
# 之后从类属性中删除该Field
# 将表名存储到__table__属性中
class ModelMetaClass(type):
    def __new__(mcs, class_name, supers, attrs):
        if class_name == 'Model':
            return type.__new__(mcs, class_name, supers, attrs)
        print('Found model: {0}'.format(class_name))
        mappings = dict()
        for key, value in attrs.items():
            if isinstance(value, Field):
                print('Found mapping: {0} ==> {1}'.format(key, value))
                mappings[key] = value

        for key in mappings.keys():
            attrs.pop(key)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = class_name
        return type.__new__(mcs, class_name, supers, attrs)


# Model父类
class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Model' object has no attribute {0}".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        args = []
        for key, value in self.__mappings__.items():
            fields.append(value.name)
            args.append(getattr(self, key, None))
        sql = 'insert into {0} ({1}) values ({2})'\
            .format(self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL:{0}'.format(sql))
        print('ARGS: {0}'.format(str(args)))


# 用户类
# User会隐式继承Model的元类ModelMetaClass
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    password = StringField('password')


class Data(Model):
    id = IntegerField('id')
    data = StringField('data')


if __name__ == '__main__':
    user = User(id=123, name='Batman', password='abcde')
    print()
    user.save()

    data = Data(id=456, data='qwert')
    print()
    data.save()

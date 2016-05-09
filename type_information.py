#获取对象信息
print('type(123)', type(123))
print('type(\'str\')', type('str'))
print('type(Nnoe)', type(None))
print('type(abs)', type(abs))

class Animal(object):
    def run(self):
        print('Animal is running...')

a = Animal()
print('type(a)', type(a))

class Dog(Animal):
    def run(self):
        print('Dog is running...')

dog = Dog()
print('isinstance(dog, Dog)', isinstance(dog, Dog))
print('isinstance(dog, Animal)', isinstance(dog, Animal))

#获取对象的属性和方法
print('str的属性和方法', dir('ABC'))

print('自定义对象的属性和方法', dir(dog))
#print((dog.__sizeof__))

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\')', hasattr(obj, 'x'))
print('hasattr(obj, \'y\')', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('hasattr(obj, \'y\')', hasattr(obj, 'y'))
print('getattr(obj, \'y\')', getattr(obj, 'y'))
print('getattr(obj, \'z\', 404)', getattr(obj, 'z', 404)) #属性不存在，返回默认值404

print('hasattr(obj, \'power\')', hasattr(obj, 'power'))
func = getattr(obj, 'power')
print('MyObject power ', func())


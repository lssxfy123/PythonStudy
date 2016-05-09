#类的继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self): #多态，子类和父类存在相同的run方法，子类的run方法会覆盖父类的run方法，同C++的虚函数有些类似
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

#静态语言（C++，Java）如果需要传人Animal类型，则必须传人Animal或其子类型
#动态语言如Python，则不需要一定传人Animal或其子类型，只需要保证传人的对象有一个run方法就行了(鸭子类型)
class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())

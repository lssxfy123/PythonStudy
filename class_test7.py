#多重继承
class Animal(object):
    pass

#哺乳类
class Mammal(Animal):
    pass

#鸟类
class Bird(Animal):
    pass

#能跑的
class Runnable(object):
    def run(self):
        print('Running...')

#能飞的
class Flyable(object):
    def fly(self):
        print('Flying...')

#多重继承
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

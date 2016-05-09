#定制类
class Student(object):
    def __init__(self, name): #有点类似C++中的构造函数
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

s = Student('Michael')
print(s)

#定制可以迭代的类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
          return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)



#限制实例的属性
class Student(object):
    __slots__ = ('name', 'age') #允许绑定属性name，age

s = Student()
s.name = 'Michael'
s.age = 25
#s.score = 99 #error，no attribute 'score'

#__slots__只对当前类实例有效，对子类不起作用
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99

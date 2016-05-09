#实例属性和类属性
#Python是动态语言，根据类创建的实例可以任意绑定属性，这是实例属性
#在类中定义的属性为类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)

s.name = 'Michael'
print(s.name)
print(Student.name)

del s.name #删除实例的属性
print(s.name)

#实例属性和类属性千万不要用相同的名称，否则类属性会被屏蔽掉


#类和实例
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s'% (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 60)

print('name %s, score %f'% (bart.name, bart.score))
bart.print_score()
print(bart.get_grade())

#Python允许实例变量绑定任何数据，同一个类的两个不同的实例对象，有可能拥有不同的变量
lisa = Student('Lisa Simpson', 87)
bart.age = 9

#print(lisa.age) #error

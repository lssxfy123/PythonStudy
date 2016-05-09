#类的访问控制
class Student(object):
    def __init__(self, name, score):
        self.__name = name  # private变量，名称前面加两个下划线
        self.__score = score  # private变量
    def print_score(self):
        print('%s: %s'% (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else :
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
#print(bart.__name)
bart.print_score()
bart.set_score(88)

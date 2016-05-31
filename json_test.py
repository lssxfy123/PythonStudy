#json序列化
import json
d = {'name': 'Bob', 'age' : 20, 'score' : 80}
print(json.dumps(d))

L = [1, 2, 3, 4, None]
print(json.dumps(L))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

print(json.dumps(s, default = lambda obj: obj.__dict__))

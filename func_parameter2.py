#可变参数的函数
#可变参数在函数调用时自动组装为一个tuple
def calc(*nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum

print("calc null", calc())
print("calc ", calc(1, 2))
print("calc too ", calc(1, 3, 5, 7))

nums = [1, 2, 3]

#*nums表示将nums的所有元素作为可变参数传进函数
print("calc nums", calc(*nums))
print("print nums", *nums)
print("print nums too", nums)

#关键字参数
#关键字参数允许传入任意个含有参数名的参数，在函数调用时组装成一个dict
def person(name, age, **key_word):
    print('name:', name, 'age:', age, 'others:', key_word)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')
person('Adam', 45, gender = 'M', job = 'Engineer')

extra = {'city' : 'New York', 'job' : 'police'}
person('Jack', 34, **extra)

#命名关键字参数
#关键字参数的名称是限定的
#*分隔符不能缺少，否则编译器无法识别位置参数和命名关键字参数
#name,age是位置参数，city,job是命名关键字参数
def person(name, age, *, city, job):
    print('name:', name, 'age', age, 'city', city, 'job', job)

person('Jack', 34, city = 'New York', job = 'police')

#命名关键字参数调用时，如果没有默认值，必须传入参数名
#person('Jack', 34, 'New York', 'police')  error

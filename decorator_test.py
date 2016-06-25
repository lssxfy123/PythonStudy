#装饰器
#函数是一个对象，可以赋给变量，通过变量来调用该函数

def now():
    print('2016-05-06')

f = now
f()

print('func name', now.__name__)

#在代码运行期间动态增加功能的方式，称为装饰器decorator
import functools

#装饰器接收一个函数作为参数
def log(func):
    @functools.wraps(func) #将原始函数的__name__等属性复制到wrapper()函数中
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper #返回一个函数

#相当于执行date = log(date)
@log
def date():
    print('2016-05-06')

#log()是一个decorator，所以原来的date()仍然存在，只是现在同名的date变量指向了新的函数
#执行date()将指向新的函数，即在log()函数中返回的wrapper()函数
#wrapper()函数的参数定义为(*args, **kw)可以接受任意参数的调用
date()

#装饰器本身传人参数
#三层嵌套
def log(text = 'none'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'% (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#time = log('excute')(time)
@log('excute')
def time():
    print('13:42:05')

time()

@log()
def date():
    print('2016-05-06')

date()

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s()'% func.__name__)
        func()
        print('end call %s()'% func.__name__)
    return wrapper

@log
def f():
    print('foo')

f()
print('f() name', f.__name__)




#Python中，函数可以赋给变量
print('abs(-10)', abs(-10))

f = abs
print('f(-10)', f(-10))

#函数名也是变量，有点类似C++的函数指针
#add的参数能接收别的函数，称为高阶函数
def add(x, y, func):
    return func(x) + func(y)

print("add(-5, 6, abs)", add(-5, 6, abs))

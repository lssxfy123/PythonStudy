#偏函数
import functools
int2 = functools.partial(int, base = 2)
print(int2('10000000'))

#functools.partial将一个函数的某些参数固定住（设置默认值），返回一个偏函数

print(int2('100000', base = 10))

#创建偏函数时，接收函数对象，*args和**kw这3个参数
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))

#相当于
args = (10, 5, 6, 7)
print(max(*args))

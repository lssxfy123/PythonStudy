#函数调用
a = abs(-100)
print('abs func', a)

b = max(2, 3, 1, -5)
print('max func', b)

c = int('123')
print('str to int', c)

#定义函数
def MyAbs(x):
#定义参数类型的检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
	    return x
    else:
	    return -x

d = MyAbs(-5)
print('user defined abs', d)

#MyAbs('a')

#返回多个值得函数，返回的是一个tuple

#导入Python自带的数学包
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print('return multi-result', r)
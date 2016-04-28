#reduce函数
#reduce接收两个参数(最多接收3个)，一个是函数(必须是二元函数)，另一个是Iterable，但其返回值不是Iterator
#reduce将结果继续和序列的下一个元素进行计算，返回最终的结果
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
    return x * 10 + y

print('[1, 3, 5, 7, 9]convert to int', reduce(fn, [1, 3, 5, 7, 9]))

#字符转换为整数
def char2num(s):
    return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]

print(list(map(char2num, '13579')))

#字符串转换为整数
def str2int(s):
    return reduce(fn, map(char2num, s))

print('\'13579\' convert to int', str2int('13579'))

#字符串首字母大写
def normalize(name):
    return name.title()

L1 = ['aDma', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#求列表的乘积
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

print('1 * 3 * 5 * 7 * 9 = ', prod([1, 3, 5, 7, 9]))

#reduce()函数接收3个参数
def prod1(L, start_value):
    def fn(x, y):
        return x * y
    return reduce(fn, L, start_value)

result = prod1([3, 5, 7], 2)
print(result) # 2 * 3 * 5 * 7=210

result = prod1([3, 5, 7], 'a')
print(result) # 'aaaa...'105个a

result = prod1([3, 5, 7], ['a', 'b'])
print(result) # ['a', 'b', 'a', 'b', ...]105个['a', 'b']



#字符串转换为浮点数
def str2float(s):
    def char2float(s):
        return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '.' : -1}[s]
    nums = map(char2float, s)
    #print(list(nums))
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)
             
    
print(str2float('.456'))


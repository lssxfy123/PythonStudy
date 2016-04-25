#位置参数,类似C++中的形参
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print("5的2次方", power(5, 2))

#默认参数的函数
def power1(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print("6的2次方", power1(6))
print("6的3次方", power1(6, 3))

#函数的默认参数在定义时一定要是一个不可变对象，如str，None等，不要定义成list，否则会出现下面的问题
def AddEnd(L = []):
    L.append("END")
    return L

print("add end ", AddEnd())
print("add end too ", AddEnd())

#可以看出默认值发生了变化，相同的调用，结果不同
def AddEnd1(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

print("add end", AddEnd1())
print("add end too", AddEnd1())
print("add abc end ", AddEnd1(['a', 'b', 'c']))
#print("add 123 end", AddEnd1('123'))




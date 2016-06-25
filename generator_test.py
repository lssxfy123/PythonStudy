#生成器
#列表生成式直接创建一个列表，这样会占用大量的内存空间。
#如果列表元素可以按照某种算法推算出来，就可以利用生成器
#一边循环一边处理后续的元素，从而节省内存空间

#列表生成式
L = [x * x for x in range(10)]

#生成器
G = (x * x for x in range(10))

for item in G:
    print(item)

#如果函数中使用了关键字yield，则函数变成了一个生成器generator
def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield b
        temp = a
        a = b
        b = temp + b
        n = n + 1
    return 'done'

#执行普通函数时，遇到return或函数最后一行就会返回，而执行generator函数时，则是遇到yield语句返回，下次执行时从上次返回的yield
for item in fib(6):
    print(item)


def fib1(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield b
        a, b = b, a + b #参考Python中的多重赋值
        n = n + 1
    return 'done'

#这样不会得到函数中的return返回值
for item in fib1(6):
    print(item)

#如果希望拿到return返回值，需要捕获错误
G = fib(6)
while True:
    try:
        x = next(G)
        print(x)
    except StopIteration as e:
        print("Generator return value", e.value)
        break

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

for item in odd():
    print(item)


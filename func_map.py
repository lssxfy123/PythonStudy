#map函数
#map接收两个参数，一个是函数，另一个是Iterable
#map将传人的函数作用到每一个序列元素，并将结果作为一个新的Iterator返回
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7])

for item in r:
    print(item)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#map()函数接收的参数的数目有其第一个函数参数决定
#map()参数的数目是函数参数数目+1，除了第一个函数参数，其余参数必须是Iterable
r = map(power, [1, 2, 3, 4, 5], [4])
print(list(r)) # [power(1, 4)]1个元素

r = map(power, [1, 2, 3, 4, 5], [4, 5])
print(list(r)) # [power(1, 4), power(2, 5)]2个元素

r = map(power, [1, 2, 3, 4, 5], [4, 5, 3])
print(list(r)) # [power(1, 4), power(2, 5), power(3, 3)]3个元素

r = map(power, [1, 2, 3, 4, 5], [4, 5, 3, 2, 2])
print(list(r)) # [power(1, 4), power(2, 5), power(3, 3), power(4, 2), power(5, 2)]5个元素

r = map(power, [1, 2, 3, 4, 5], [4, 5, 3, 2, 2, 4, 7])
print(list(r)) # [power(1, 4), power(2, 5), power(3, 3), power(4, 2), power(5, 2)]5个元素


print('int [1, 2, 3, 4, 5, 6] convert str', list(map(str, [1, 2, 3, 4, 5, 6])))


#匿名函数lambda
print(list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#lambda x : x * x相当于
#def f(x):
#    return x * x

#关键字lambda表示匿名函数，冒号前面表示函数参数
#匿名函数只能有一个表达式，返回值为该表达式的结果
#匿名函数也是一个函数表达式，可以将匿名返回赋给一个变量
f = lambda x : x * x
print(f(5))

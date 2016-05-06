#函数返回值是一个函数
def lazy_sum(*args): #可变参数
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum  #返回一个函数

f = lazy_sum(1, 3, 5, 7, 9)

#调用f时，才会真正计算求和结果
print("sum = ", f())

#返回函数的程序是闭包
#返回的函数sum可以使用外部函数lazy_sum的局部变量args
#当lazy_sum返回sum后，其局部变量args还会被使用，所以
#返回函数不要引用任何后期会发生变化的变量


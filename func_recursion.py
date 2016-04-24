#递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print("10的阶乘", fact(10))
print("100的阶乘", fact(100))

#汉诺塔移动
def Hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    Hanoi(n - 1, a, c, b)
    print(a, '-->', c)
    Hanoi(n - 1, b, a, c)

Hanoi(3, 'A', 'B', 'C')

#filter()函数用于过滤序列
#filter()函数和map函数类似，接收一个函数和一个序列，不同的是filter必须接收两个参数，所以其函数参数必须只有一个位置参数
#filter()把传入的函数作用每个元素，然后根据返回值时True还是False决定保留还是丢弃该元素
#filter()返回值也是个Iterator
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A','','b', None, 'C', ' '])))

def max(x, y = 3):
    return x > y

print(list(filter(max, [1, 4, 5])))

#无线奇数序列，生成器
def odd_iter():
    n = 1
    while True: #无限循环
        n = n + 2;
        yield n

def not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it = odd_iter()  #初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(not_divisible(n), it) #构造新的序列，n=3表示新的序列中没有3的倍数

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#回文数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

#函数参数的组合
#函数参数分为：必选参数（位置参数），默认参数，可变参数，关键字参数和命名关键字参数
#其中，可变参数和命名关键字参数无法混合，其余皆可组合使用
#参数顺序的定义必选是：必选参数，默认参数，可变参数/命名关键字参数，关键字参数
def func1(a, b, c = 0, *args, **key_word):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'key_word =', key_word)

def func2(a, b, c = 0, *, d, **key_word):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'key_word =', key_word)

func1(1, 2)
func1(1, 2, 3)
func1(1, 2, 3, 'a', 'b')
func1(1, 2, 3, 'a', 'b', x = 99)


func2(1, 2, 3, d = 'a', ext = None)

#通过tuple和dict也可以调用上述函数
args = (1, 2)
func1(*args) #等同于func1(1, 2)

args = (1, 2, 3)
func1(*args) #等同于func1(1, 2, 3)

args = (1, 2, 3, 'a', 'b')
func1(*args) #等同于func1(1, 2, 3,'a', 'b')

args = (1, 2, 3, 'a', 'b')
key_word = {'x' : 99}
func1(*args, **key_word) #等同于func1(1, 2, 3, 'a', 'b', x = 99)

args = (1, 2, 3)
key_word = {'d' : 'a', 'ext' : None}
func2(*args, **key_word) #等同于func2(1, 2, 3, d = 'a', ext = None)

#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它

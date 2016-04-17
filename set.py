#set类似dict，但不存储value
s =set([1, 2, 3])
print('set ', s)

#set会自动过滤重复元素
s = set([1, 1, 2, 2, 3, 3])
print('set', s)

s.add(5)
print('add set', s)

s.remove(1)
print('remove set', s)

#set可以进行数学意义上的交集，并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2
print('s1 & s2', s3)

s4 = s1 | s2
print('s1 | s2', s4)

#可变对象与不可变对象

#可变对象，如list
a = ['c', 'a', 'b']
print("可变对象，调用自身的排序前", a)
a.sort()
print("可变对象，调用自身的排序后", a)

#不可变对象，如str
c = 'abc'
print('不可变对象，调用自身的替代方法前', c)
d = c.replace('a', 'A')
print('不可变对象，调用自身的替代方法后', c)

#不可变对象在调用自身的替换方法，返回的是一个新的对象
print('return ', d)
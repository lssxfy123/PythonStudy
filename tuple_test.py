t = (1, 2)
print("tuple: ", t)

t1 = (1,)
print("one element tuple: ", t1)

#"可变"的tuple
#tuple元素的指向不能变，但指向的这个元素是可变的
#类似于C++中的指针常量
t2 = ('a', 'b', ['A', 'B'])
print("t2 ", t2)
t2[2][0] = 'X'
t2[2][1] = 'Y'
print("changed t2", t2)

#对象和引用

values = [0, 1, 2]
values[1] = values
print(values) #赋值无限次

values = [0, 1, 2]
values[1] = values[:]
print(values) #[0,[0, 1, 2], 2]

a = [0, [1, 2], 3]
b = a[:]
a[0] = 8
a[1][1] = 9

print(a)
print(b)

import copy
a = [0, [1, 2], 3]
b = copy.deepcopy(a)
a[0] = 8
a[1][1] = 9

print(a)
print(b)



#可变对象和不可变对象
a = "test"
a_list = [1, 2]
print(id(a))#
print(id(a_list))


a = "abc"
a_list = [1, 2]

print(id(a))
print(id(a_list))

b_list = a_list

b_list[0] = 4

print(a_list)  # [4, 2]
print(b_list)  # [4, 2]

a_list += [5, 6]

print(a_list)  # [4, 2, 5, 6]
print(b_list)  # [4, 2, 5, 6]

a_list = a_list + [7, 8]  #创建了新的对象

print(a_list)  # [4, 2, 5, 6, 7, 8]
print(b_list)  # [4, 2, 5, 6]

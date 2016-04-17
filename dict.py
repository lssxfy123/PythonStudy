#dict 类似C++中的map
d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
print("dict ", d)
print("dict element Michael", d['Michael'])

d['Adam'] = 80

#dict中的存储顺序是随机的
print("dict", d)

if 'Thomas' in d:
    print("Thomas is exist in d")
else:
    print("Thomas is not exist in d")

print('d.get(\'Bob\')', d.get('Bob'))

#删除
d.pop('Bob')
print('delete Bob', d)

#dict的key值必须是不可变的，不能为list
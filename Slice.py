#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#L[0:3]表示从索引0开始直到索引3为止，但不包括索引3
print('L', L)
print('L[0:3]', L[0:3])
print('L[:3]', L[:3])
print('L[1:3]', L[1:3])

#倒数的切片
print('L[-2:-1]', L[-2:-1])
print('L[-3:-1]', L[-3:-1])

L1 = list(range(100))
print('L1', L1)
print('L1[:10]', L1[:10])

#前10个数每2个取一个
print('L1[:10:2]', L1[:10:2])

#所有数每5个取一个
print('L1[::5]', L1[::5])

#复制list
L2 = L1[:]
print('copy L1: L1[:]', L2)

#tuple切片
T = tuple(range(50))
print('T', T)
print('T[:3]', T[:3])

#字符串切片
str = 'abcdefg'
print('str', str)
print('str[:3]', str[:3])
print('str[::2]', str[::2])
#对象和引用
L = [1, 2, 3]
D = {'a' : 1, 'b' : 2}
A = L[:]
B = D.copy()

print(L, D)
print(A, B)

print(id(L))
print(id(A))

A[1] = 'NI'
B['c'] = 'spam'
print(L, D)
print(A, B)

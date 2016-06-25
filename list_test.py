classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print("list len = ", len(classmates))
print("first element: ", classmates[0])
print("second element: ", classmates[1])
print("third element: ", classmates[2])

print("last element: ", classmates[-1])

classmates.append('Adam')
print("append list: ", classmates)

classmates.insert(1, 'Jack')
print("insert list at 1: ", classmates)

classmates.pop()
print("delete the last element: ", classmates)

classmates.pop(1)
print("delete the second element: ", classmates)

classmates[1] = 'Sarah'
print("replace the second element: ", classmates)

s = ['python', 'java', ['asp', 'php'], 'C++']
print("list element is a list: ", s)

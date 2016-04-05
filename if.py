age = 3
if age >= 18:
    print("your age is ", age)
    print("adult")
elif age >= 6:
    print("your age is ", age)
    print("teenager")
else:
    print("your age is ", age)
    print("kid")

s = input("birth: ")
age = int(s)
if age <= 2000:
    print("00前")
else:
    print("00后")


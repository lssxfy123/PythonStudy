
def func_int(a):
    a+= 4
   
def func_list(a_list):
    a_list[0] = 4

t = 0
func_int(t)
print(t)  # t = 0

t_list = [1, 2, 3]
func_list(t_list)
print(t_list)  # t_list = [4, 2, 3]

list_a = []
def func_list1():
    list_a = [1]

func_list1()
print(list_a)  #[]

print("=======================")

list_b = []

def func_list2():
    list_b.append(1)

func_list2()

print(list_b)  # [1]

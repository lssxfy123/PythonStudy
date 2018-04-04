# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.3
# while循环
current_number = 1
while current_number <= 5:
    print("current number: " + str(current_number))
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# break
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

print()

# continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

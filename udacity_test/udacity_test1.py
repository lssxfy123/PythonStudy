# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.6
# python练习测试
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay", "Tom Jack Lee"]
for name in names:
    print('_'.join(name.lower().split(' ')))

for name in names:
    name = name.lower().replace(" ", "_")
print(names)  # 没有任何变化

for i in range(len(names)):
    names[i] = names[i].lower().replace(" ", "_")
print(names)


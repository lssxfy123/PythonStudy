# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.10
# 文件写入

# 类似C语言中的文件写入
# 如果不存在会创建文件
# 会覆盖原来的内容
with open('测试.txt', 'w') as file_object:
    file_object.write("Python文件测试\n")
    file_object.write("Python学习\n")
print()

# 附加模式写入
with open('测试.txt', 'a') as file_add:
    file_add.write("Python开发工具\n")

print("包含中文的string")

print("A的ASCII码", ord('A'))
print("中的Unicode码", ord('中'))

print("65对应的字符",chr(65))
print("25991对应的文字", chr(25991))

#字符串转换为bytes
x = 'ABC'.encode("ascii")
print("字符串转换为bytes", x)

x = '中文'.encode('utf-8')
print("字符串转换为bytes", x)
print("len = ", len(x))
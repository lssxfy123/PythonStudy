#base64编码
import base64
b1 = base64.b64encode(b'binary')
print(b1)
d1 = base64.b64decode(b1)
print(d1)
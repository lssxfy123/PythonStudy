from PIL import Image
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((400, 300))
im.save('thumb.jpg', 'JPEG')

from PIL import Image

img = Image.open('westbrook.jpg')
out = img.point(lambda i:(int)(i * 0.5))
out.save('Q2.jpg', 'JPEG')

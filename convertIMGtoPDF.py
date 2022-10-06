from email.mime import image
from PIL import Image

img1 = Image.open("cat.jpg")
image1 = img1.convert('RGB')
image1.save('cat.pdf')
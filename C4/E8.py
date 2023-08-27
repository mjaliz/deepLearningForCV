from PIL import Image
from numpy import asarray

image = Image.open("opera_house.jpg")

data = asarray(image)
print(data.shape)

image2 = Image.fromarray(data)

print(image2.format)
print(image2.mode)
print(image2.size)

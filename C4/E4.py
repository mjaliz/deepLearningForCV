from PIL import Image

image = Image.open("opera_house.jpg")

print(image.format)
print(image.mode)
print(image.size)

image.show()

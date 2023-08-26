# Create a thumbnail of an image
from PIL import Image

image = Image.open("opera_house.jpg")
print(image.size)
# create a thumbnail and preserve aspect ratio
image.thumbnail((100, 100))
print(image.size)
image.show()

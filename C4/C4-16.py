# Resize image and force a new shape
from PIL import Image

image = Image.open("opera_house.jpg")
print(image.size)
# resize image and ignore original aspect ratio
img_resized = image.resize((200, 200))

print(img_resized.size)
img_resized.show()

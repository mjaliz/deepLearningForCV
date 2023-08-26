from PIL import Image

image = Image.open("opera_house.jpg")

image.save("opera_house.png", format="PNG")

image2 = Image.open("opera_house.png")
print(image2.format)

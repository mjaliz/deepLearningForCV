# Example of saving a grayscale version of a loaded image
from PIL import Image

image = Image.open("opera_house.jpg")

gs_image = image.convert(mode="L")
gs_image.save("opera_house_grayscale.jpg")

image2 = Image.open("opera_house_grayscale.jpg")
image2.show()

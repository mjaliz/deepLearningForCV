# Create rotated version of an image
import os
from PIL import Image
from matplotlib import pyplot

current_dir = os.path.realpath(os.path.dirname(__file__))

image = Image.open(os.path.join(current_dir, "opera_house.jpg"))

pyplot.subplot(311)
pyplot.imshow(image)

pyplot.subplot(312)
pyplot.imshow(image.rotate(45))

pyplot.subplot(313)
pyplot.imshow(image.rotate(90))

pyplot.show()

# Example of cropping an image
import os
from PIL import Image

current_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(current_dir, "opera_house.jpg"))

cropped = image.crop((100, 100, 200, 200))
cropped.show()

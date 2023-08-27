# Load and show image with Pillow
import os
from PIL import Image

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))

print(image.format)
print(image.size)
print(image.mode)

image.show()

# Example of global pixel standardization
import os
from PIL import Image
from numpy import asarray

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))
pixels = asarray(image)
pixels = pixels.astype("float32")

mean, std = pixels.mean(), pixels.std()
print("Mean: %.3f, Standard Deviation: %.3f" % (mean, std))

# global standardization of pixels
pixels = (pixels - mean) / std
mean, std = pixels.mean(), pixels.std()
print("Mean: %.3f, Standard Deviation: %.3f" % (mean, std))

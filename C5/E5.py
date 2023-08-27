# Example of global centering (subtract mean)
import os
from numpy import asarray
from PIL import Image

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))
pixels = asarray(image)
pixels = pixels.astype("float32")
mean = pixels.mean()

print("Mean: %.3f" % mean)
print("Min: %.3f, Max: %.3f" % (pixels.min(), pixels.max()))

pixels = pixels - mean

mean = pixels.mean()
print("Mean: %.3f" % mean)
print("Min: %.3f, Max: %.3f" % (pixels.min(), pixels.max()))

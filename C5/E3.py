# Example of pixel normalization
import os
from numpy import asarray
from PIL import Image

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))
pixels = asarray(image)

print("Data Type: %s" % pixels.dtype)
print("Min: %.3f, Max: %.3f" % (pixels.min(), pixels.max()))

pixels = pixels.astype("float32")
pixels /= 255.0

print("Min: %.3f, Max: %.3f" % (pixels.min(), pixels.max()))

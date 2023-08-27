# Example of global pixel standardization shifted to positive domain
import os
from numpy import asarray
from numpy import clip
from PIL import Image

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))
pixels = asarray(image)
pixels = pixels.astype("float32")

mean, std = pixels.mean(), pixels.std()
print("Mean: %.3f, Standard Deviation: %.3f" % (mean, std))

# global standardization of pixels
pixels = (pixels-mean)/std
# clip pixel values to [-1,1]
pixels = clip(pixels, -1.0, 1.0)
# shift from [-1,1] to [0,1] with 0.5 mean
pixels = (pixels + 1)/2.0

mean, std = pixels.mean(), pixels.std()
print("Mean: %.3f, Standard Deviation: %.3f" % (mean, std))
print("Min: %.3f, Max: %.3f" % (pixels.min(), pixels.max()))

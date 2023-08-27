# Example of per-channel centering (subtract mean)
import os
from PIL import Image
from numpy import asarray

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))

pixels = asarray(image)
pixels = pixels.astype("float32")

means = pixels.mean(axis=(0, 1), dtype="float64")
print("Means: %s" % means)
print("Mins: %s, Max: %s" % (pixels.min(axis=(0, 1)), pixels.max(axis=(0, 1))))

pixels -= means
means = pixels.mean(axis=(0, 1), dtype="float64")
print("Means: %s" % means)
print("Mins: %s, Max: %s" % (pixels.min(axis=(0, 1)), pixels.max(axis=(0, 1))))

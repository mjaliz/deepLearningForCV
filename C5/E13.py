# Example of per-channel standardization
import os
from PIL import Image
from numpy import asarray

curr_dir = os.path.realpath(os.path.dirname(__file__))
image = Image.open(os.path.join(curr_dir, "sydney_bridge.jpg"))
pixels = asarray(image)
pixels = pixels.astype("float32")

means = pixels.mean(axis=(0, 1), dtype="float32")
stds = pixels.std(axis=(0, 1), dtype="float32")
print("Means: %s, Stds: %s" % (means, stds))

pixels = (pixels - means) / stds

means = pixels.mean(axis=(0, 1), dtype="float32")
stds = pixels.std(axis=(0, 1), dtype="float32")
print("Means: %s, Stds: %s" % (means, stds))

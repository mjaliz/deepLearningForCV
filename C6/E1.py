# Example of loading an image with Keras API
import os
from keras.preprocessing.image import load_img

curr_dir = os.path.realpath(os.path.dirname(__file__))
img = load_img(os.path.join(curr_dir, "bondi_beach.jpg"))

print(type(img))
print(img.format)
print(img.mode)
print(img.size)

img.show()

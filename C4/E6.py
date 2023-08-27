from matplotlib import image
from matplotlib import pyplot

data = image.imread("opera_house.jpg")

print(data.dtype)
print(data.shape)

pyplot.imshow(data)
pyplot.show()

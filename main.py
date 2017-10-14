from __future__ import print_function
from PIL import Image
from PIL import ImageFilter
from characteristics import Characteristics


directory_size = 1
#read in images from data set
for i in range(0, directory_size):
    im = Image.open('data\pic' + str(i) + '.jpg')
    im.show()
    im1 = im.filter(ImageFilter.EDGE_ENHANCE)  # can be used to enhance the edges of shapes
    im1.show()

Characteristics.set_cap(100)

#print(im.size, im.format, im.mode)
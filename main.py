from __future__ import print_function
from PIL import Image
from PIL import ImageFilter


directory_size = 1
#read in images
for i in range(0, directory_size):
    im = Image.open('pic' + str(i) + '.jpg')
    im.show()

#print(im.size, im.format, im.mode)
#im1 = im.filter(ImageFilter.EDGE_ENHANCE)

#
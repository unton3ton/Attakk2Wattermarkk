# source DISCRETE/bin/activate
# pip install ImageHash

# Code for the blogpost https://fullstackml.com/2016/07/02/wavelet-image-hash-in-python/

# https://www.plugger.ai/blog/applications-of-hashing-algorithms-on-images
import PIL
from PIL import Image
import imagehash

img = PIL.Image.open('img/3.jpg')
img1 = PIL.Image.open('img/3-withText450-DWT-telega.jpg')

h = imagehash.phash(img)
h1 = imagehash.phash(img1)

print(h-h1)

a = imagehash.average_hash(img)
a1 = imagehash.average_hash(img1)

print(a-a1)

w = imagehash.whash(img)
w1 = imagehash.whash(img1)

print(w-w1)


c = imagehash.colorhash(img)
c1 = imagehash.colorhash(img1)

print(c-c1)


cr = imagehash.crop_resistant_hash(img)
cr1 = imagehash.crop_resistant_hash(img1)

print(cr-cr1)

# 31
# 0
# 32
# 0
# 0.0
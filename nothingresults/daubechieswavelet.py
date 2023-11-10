# source DISCRETE/bin/activate

# pip install mahotas

# https://www.geeksforgeeks.org/mahotas-transforming-image-using-daubechies-wavelet/

# importing various libraries
import numpy as np
import mahotas

import PIL
from PIL import Image

from mahotas.thresholding import soft_threshold
from matplotlib import pyplot as plt
from os import path

# loading image
f = PIL.Image.open('img/test2.jpeg').convert('L')

# making ply gray
plt.gray()

# showing image
print("Image")
plt.imshow(f)
plt.show()

# Transform using D8 Wavelet to obtain transformed image t
t = mahotas.daubechies(f, 'D8')

# showing transformed image
print("Transformed Image")
plt.imshow(t)
plt.show()

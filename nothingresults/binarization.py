# source DISCRETE/bin/activate

# https://note.nkmk.me/en/python-numpy-opencv-image-binarization/

import cv2
import numpy as np
from PIL import Image

im = cv2.imread('img/3-withText8-DWT.jpeg')

th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

print(th)
# 128.0

cv2.imwrite('img/3-withText8-DWT_th.jpg', im_th)


im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

print(th)

cv2.imwrite('img/3-withText8-DWT_th_otsu.jpg', im_gray_th_otsu)


im_bool = im_gray > th
im_dst = np.empty((*im_gray.shape, 3))
r, g, b = 255, 128, 32

im_dst[:, :, 0] = im_bool * r
im_dst[:, :, 1] = im_bool * g
im_dst[:, :, 2] = im_bool * b

Image.fromarray(np.uint8(im_dst)).save('img/3-withText8-DWT_binarization_color.png')

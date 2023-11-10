# python3 -m venv DISCRETE
# source DISCRETE/bin/activate
# pip install --upgrade pip

# https://www.programmersought.com/article/59255237172/
# https://wavelets.pybytes.com/

# https://www.programmersought.com/article/20417019129/
# pip install opencv-python matplotlib

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image

name = "3"

img = cv2.imread(f"img/{name}.jpg", cv2.IMREAD_GRAYSCALE)



# Data type conversion Convert to floating point
# print('0\n',img)
img1 = img.astype('float')

# Perform discrete cosine transform
img_dct = cv2.dct(img1)
# print('img_dct[0] = ',img_dct[0])

# Perform log processing
img_dct_log = np.log(abs(img_dct))
print('img_dct_log[0] = ',img_dct_log[0])
print('img_dct_log[1] = ',img_dct_log[1])

# Perform inverse discrete cosine transform
# img_idct = cv2.idct(img1)
# print('3\n',img_idct)


plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('original image'),plt.xticks([]),plt.yticks([])
plt.subplot(122)
plt.imshow(img_dct_log)
# plt.imshow(img_idct)
plt.title('DCT'),plt.xticks([]),plt.yticks([])
plt.savefig(f'result/result-for-{name}.png')
plt.show()
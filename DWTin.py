# python3 -m venv QR
# source QR/bin/activate
# pip install --upgrade pip


# https://github.com/guofei9987/blind_watermark
# pip install blind-watermark

'''
Как дискретное косинусное преобразование (DCT), 
так и разложение по сингулярным значениям (SVD) 
использовались в качестве математических инструментов 
для встраивания данных в изображение.
В DCT-области коэффициенты DCT модифицируются элементами
псевдослучайной последовательности действительных значений.
В домене SVD распространенным подходом является изменение
сингулярных значений с помощью сингулярных значений визуального водяного знака.

http://www.theparticle.com/documents/DCT-SVDpaperFINAL.pdf
https://peerj.com/articles/cs-1427/#
https://www.ijcsi.org/papers/IJCSI-10-3-1-223-230.pdf
'''

# # embed watermark into image:
# blind_watermark --embed --pwd 1234 img/2.jpg "watermark text" img/embedded.png

# # extract watermark from image:
# blind_watermark --extract --pwd 1234 --wm_shape 111 img/embedded.png

# pip install segno ## (for create QR)
# pip install qreader
# deactivate


# # Embed watermark:

# from blind_watermark import WaterMark

# Numb = 102

# bwm1 = WaterMark(password_img=1, password_wm=1)
# bwm1.read_img('img/3.jpg')

# wm = "A watermark is a logo that stands for watermark and \
#         prevents copying when placed on an image or image. Sometimes \
#         it can be used not as a logo, but as a special text. When \
#         using Watermark, you can block the copy or see the original \
#         author even if there is a copy. Sometimes the site logo and \
#         sometimes different names are placed on the image or in a \
#         blocking corner to create this purpose. The picture above is \
#         an example of a watermark. "

# bwm1.read_wm(wm, mode='str')
# bwm1.embed(f'img/3-withText{Numb}-DWT.jpeg')
# # bwm1.embed(f'img/3-withText{Numb}-DWT.png')
# len_wm = len(bwm1.wm_bit)
# # print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))


# #Extract watermark:

# bwm1 = WaterMark(password_img=1, password_wm=1)
# wm_extract = bwm1.extract(f'img/3-withText{Numb}-DWT.jpeg', wm_shape=len_wm, mode='str')
# # wm_extract = bwm1.extract(f'img/3-withText{Numb}-DWT.png', wm_shape=len_wm, mode='str')
# print('Extract text = ', wm_extract)
# print('\n')

# if wm == wm_extract:
#   print("\nTrue")
# else:
#   print("\nFalse")

#####################################################################################################################################################################


from bitreverse import *

import segno

Numb = 225 # предел символов для корректного извлечения

qr_name = f"qr-Text{Numb}.png" #"watermark_qrcode.png"

qrcode = segno.make_qr("A watermark is a logo that stands for watermark and \
        prevents copying when placed on an image or image. Sometimes \
        it can be used not as a logo, but as a special text. When \
        using Watermark, you can block the copy or see t ") 


# qrcode = segno.make_qr("A watermark is a logo that stands for watermark and prevents copying when placed on an image or image.")

qrcode.save(
    f"img/{qr_name}",
    scale=2,
    light="white",
    dark="black",
    data_dark="green",
)


# Изменяем размер qr-кода для возможности добавить bit-reverse

from PIL import Image
with Image.open(f"img/qr-Text{Numb}.png") as im:
	N = 7
	N = 2**N
	im = im.resize((N, N)) # 64 и 256 требуют других размеров контейнер 
	# # сохранение картинки
	im.save(f"img/qr-Text{Numb}.png") 
	


from qreader import QReader
import cv2

# Create a QReader instance
qreader = QReader()

# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread(f"img/{qr_name}"), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text_before = qreader.detect_and_decode(image=image)
print("\n\ndecoded text before = ", decoded_text_before)


# Голограмма bitreverse

img = cv2.imread(f"img/qr-Text{Numb}.png", cv2.IMREAD_COLOR)
# шифруем
img = example2(img)
cv2.imwrite(f"img/bitrev-qr-Text{Numb}.png",img)



from blind_watermark import WaterMark

bwm1 = WaterMark(password_wm=1, password_img=1)
# read original image
bwm1.read_img('img/test2.jpeg') # изображение - контейнер
# read watermark
# bwm1.read_wm('img/watermark_qrcode.png')
bwm1.read_wm(f'img/bitrev-qr-Text{Numb}.png')
# embed
bwm1.embed(f'img/controltest-with-qr-bitrev-Text{Numb}-DWT.jpeg')



# # Extract watermark:

# from PIL import Image
# im = Image.open('img/watermark_qrcode.png')
# width, height = im.size
# # N = 7
# # N = 2**N
width, height = N, N


from blind_watermark import WaterMark
bwm1 = WaterMark(password_wm=1, password_img=1)
# notice that wm_shape is necessary
bwm1.extract(filename=f'img/controltest-with-qr-bitrev-Text{Numb}-DWT.jpeg', wm_shape=(width, height), out_wm_name=f'img/extracted_controltest-with-qr-bitrev-Text{Numb}-DWT.png', )


# расшифровываем
# применяем бит-реверсивную перестановку для востановления изображения
img = cv2.imread(f"img/extracted_controltest-with-qr-bitrev-Text{Numb}-DWT.png", cv2.IMREAD_COLOR)
img = example2(img)
cv2.imwrite(f"img/result-for-controltest-bitrev-qr-Text{Numb}.png",img)


# # # Проверка
# # # Create a QReader instance
from qreader import QReader
import cv2
qreader = QReader()

# Get the image that contains the QR code

image = cv2.cvtColor(cv2.imread(f'img/result-for-controltest-bitrev-qr-Text{Numb}.png'), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text_after = qreader.detect_and_decode(image=image)
print("\n\nextracted_img text (after)= \n", decoded_text_after)


if decoded_text_before == decoded_text_after:
	print("\nTrue")
else:
	print("\nFalse")

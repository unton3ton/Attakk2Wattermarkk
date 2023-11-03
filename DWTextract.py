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




from blind_watermark import WaterMark

Numb = 450

namefile = '3-withText450-DWT-fromtinypng.jpeg' # извлёк с небольшой помаркой "t(ere" после tinypng.com

'''
Extract text =  A watermark is a logo that stands for watermark and    
     prevents copying when placed on an image or image. Sometimes    
          it can be used not as a logo, but as a special text. When   
                using Watermark, you can block the copy or see the original  
                       author even if t(ere is a copy. Sometimes the site logo and    
                            sometimes different names are placed on the image or in a   
                                  blocking corner to create this purpose. The picture above is   
                                        an example of a watermark.
'''


#'3-withText450-DWT.jpeg'
#'3-withText450-DWT-after.jpg' # после https://picwish.com/remove-unwanted-object извлёк с повреждениями

'''
Extract text =  A(3atermarc �s a 
 kgO thaD stands fnb wa4eR-ar+ af%  
   ( $ prmvents coty)ng 7hdn!0lace$ol aN0mmagE op imafe Qometymes  
          (t can be uS�d fota3a lngk, ruD0a� A2pec)aL �a8t. Uhej 
             0    usmn& Va4ermARk, iou +a* blmcj dh% ckpy o2 sed e o�ig)nad 
              (  (   aethmr(e6en id thDra is a c/p{. Ro-euImEs t�e site loeM and  "  
                  soedtioes `mbf�RE�t`.aI%3�!pe p,ace� mn"the iiag% nr0i, A    
                      �bl�c+hnF a~rner tk bre�e this 0qrpose.0THa p)Cp5ra ab/ve(ir`  
                       !`  an %pAepHa ofq 7Apar5ark. 

'''

'1-withText102-DWT.jpg'

# #Extract watermark:
bwm1 = WaterMark(password_img=1, password_wm=1)

wm = 'A watermark is a logo that stands for watermark and \
        prevents copying when placed on an image or image. Sometimes \
        it can be used not as a logo, but as a special text. When \
        using Watermark, you can block the copy or see the original \
        author even if there is a copy. Sometimes the site logo and \
        sometimes different names are placed on the image or in a \
        blocking corner to create this purpose. The picture above is \
        an example of a watermark. ' #"watermark"

bwm1.read_wm(wm, mode='str')

len_wm = len(bwm1.wm_bit)
# print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))



wm_extract = bwm1.extract(f'img/{namefile}', wm_shape=len_wm, mode='str')
# wm_extract = bwm1.extract('img/3-withText1000-DWT.png', wm_shape=len_wm, mode='str')
print('Extract text = ', wm_extract)
print('\n')

if wm == wm_extract:
  print("\nTrue")
else:
  print("\nFalse")

###################################################################################################################################################################

# from bitreverse import *

# import segno

# Numb = 225 # кол-во символов watermark
# # ziip = '_vk'
# namefile = 'fromtinypng.jpeg' # extracted_img text (after)= (None,)
# #'roter.jpeg' # extracted_img text (after)=  (None,) без сжатия -- просто поворот на 180 градусов в графредакторе
# #'removeWM.jpg' # extracted_img text (after)= (None,)
# #'removeWM1.jpg' # extracted_img text (after)= (None,)

# #'vk.jpg' # извлёк
#  #'telega.jpg' # извлёк
# # 'controltest-with-qr-bitrev-Text225-DWT.jpeg'

# #'controltest-with-qr-bitrev-Text225-DWT-vk.jpg' # assert self.wm_size < self.block_num, IndexError
# #'controltest-with-qr-bitrev-Text225-DWT-telegram.jpg' # assert self.wm_size < self.block_num, IndexError
# #f'controltest-with-qr-bitrev-Text{Numb}-DWT.jpeg'
# #'3-with-qr-bitrev-Text225-DWT-after.jpg' # после https://picwish.com/remove-unwanted-object не сработал
# #'3-with-qr-bitrev-Text225-DWT-transformed.jpeg' # after https://www.watermarkremover.io/ru/upload сработал


# N = 7
# N = 2**N
# width, height = N, N


# from blind_watermark import WaterMark
# bwm1 = WaterMark(password_wm=1, password_img=1)
# # notice that wm_shape is necessary
# bwm1.extract(filename=f'img/{namefile}', wm_shape=(width, height), out_wm_name=f'img/extracted_controltest-with-qr-bitrev-Text{Numb}-DWT.png', )


# # расшифровываем
# # применяем бит-реверсивную перестановку для востановления изображения
# img = cv2.imread(f"img/extracted_controltest-with-qr-bitrev-Text{Numb}-DWT.png", cv2.IMREAD_COLOR)
# img = example2(img)
# cv2.imwrite(f"img/result-for-controltest-bitrev-qr-Text{Numb}.png",img)


# # # # Проверка
# # # # Create a QReader instance
# from qreader import QReader
# import cv2
# qreader = QReader()

# # Get the image that contains the QR code

# image = cv2.cvtColor(cv2.imread(f'img/result-for-controltest-bitrev-qr-Text{Numb}.png'), cv2.COLOR_BGR2RGB)

# # Use the detect_and_decode function to get the decoded QR data
# decoded_text_after = qreader.detect_and_decode(image=image)
# print("\n\nextracted_img text (after)= \n", decoded_text_after)

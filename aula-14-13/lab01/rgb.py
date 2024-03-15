import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

#abre imagem
filename = sys.argv[1]

im = cv2.imread(filename)

#converte cores
im_in_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

#split
im_h,im_s,im_v = cv2.split(im_in_hsv)

im_h = im[:,:,0]
im_s = im[:,:,1]
im_v = im[:,:,2]



#combina as imagens
im = cv2.merge([im_h,im_s,im_v])

#mostra imagens
imagens = [im_h,im_s,im_v]



x_values = np.arange(256)

plt.subplot(1,3,1),plt.imshow(imagens[0],cmap = 'gray')
plt.subplot(1,3,2),plt.imshow(imagens[1],cmap = 'gray')
plt.subplot(1,3,3),plt.imshow(imagens[2],cmap = 'gray')



plt.show()













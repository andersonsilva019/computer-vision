import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Gamma Correction with look-up table
def gamma_correction_with_lut(img, gamma):
  # g(x,y) = ((f(x,y)/255)^(1/gamma)) * 255 where f(x,y) is the pixel value of the input image 

  # split the image into RGB channels
  im_r, im_g, im_b = cv.split(img)

  # create a look-up table
  lookUpTable = np.empty((1,256), np.uint8)

  # fill the look-up table
  for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, 1/gamma) * 255.0, 0, 255)

  # apply the look-up table
  im_g = cv.LUT(im_g, lookUpTable)
  im_b = cv.LUT(im_b, lookUpTable)

  return cv.merge((im_r, im_g, im_b))

# Gamma Correction without look-up table
def gamma_correction(img, gamma):
  # g(x,y) = (f(x,y)/255)^(1/gamma) * 255 where f(x,y) is the pixel value of the input image 

  # split the image into RGB channels
  im_r, im_g, im_b = cv.split(img)

  # apply the gamma correction  
  im_g = np.clip(pow(im_g / 255.0, 1/gamma) * 255, 0, 255)

  # apply the gamma correction
  im_b = np.clip(pow(im_b / 255.0, 1/gamma) * 255, 0, 255)

  # convert the image to 8-bit unsigned integer
  im_g = np.uint8(im_g) 
  im_b = np.uint8(im_b)

  return cv.merge((im_r, im_g, im_b))

def main():
  #load image
  filename = sys.argv[1]
  img = cv.imread(filename)

  plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
  plt.title('Original image')
  plt.subplot(2, 2, 2), plt.imshow(cv.cvtColor(gamma_correction_with_lut(img, 2), cv.COLOR_BGR2RGB))
  plt.title('Gamma = 2')
  plt.subplot(2, 2, 3), plt.imshow(cv.cvtColor(gamma_correction_with_lut(img, 3), cv.COLOR_BGR2RGB))
  plt.title('Gamma = 3')
  plt.subplot(2, 2, 4), plt.imshow(cv.cvtColor(gamma_correction_with_lut(img, 4), cv.COLOR_BGR2RGB))
  plt.title('Gamma = 4')

  plt.show()

main()
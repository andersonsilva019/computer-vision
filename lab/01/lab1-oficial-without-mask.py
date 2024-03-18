import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def isGreenInHSV(value):
  return value >= 30 and value <= 80

def isBlueHsv(value):
  return value >= 90 and value <= 140

img = cv2.imread("gamora_nebula.jpg")

img_in_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
img_h_channel, img_s_channel, img_v_channel = cv2.split(img_in_hsv)

for i,c in enumerate(img_h_channel):
  for j,pixel in enumerate(c):
    if isGreenInHSV(pixel):
      img_h_channel.itemset(i,j, 120)
    elif isBlueHsv(pixel):
      img_h_channel.itemset(i,j, 50)

new_img = cv2.merge([img_h_channel, img_s_channel, img_v_channel])

# convert to RGB
new_img = cv2.cvtColor(new_img, cv2.COLOR_HSV2BGR)

# show the image
cv2.imshow("Image", new_img)

cv2.waitKey(0)

cv2.destroyAllWindows()










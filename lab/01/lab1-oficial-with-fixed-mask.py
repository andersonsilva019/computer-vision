import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

title_window = "Slider"

def isGreenInHSV(value):
  return value >= 30 and value <= 80

def isBlueHsv(value):
  return value >= 90 and value <= 140

def maskBlue(img_in_hsv):
  lower_blue = np.array([83, 0, 0])
  upper_blue = np.array([107, 255, 255])
  mask = cv2.inRange(img_in_hsv, lower_blue, upper_blue)
  return mask

def maskGreen(img_in_hsv):
  lower_green = np.array([4, 0, 0])
  upper_green = np.array([83, 255, 255])
  mask = cv2.inRange(img_in_hsv, lower_green, upper_green)
  return mask

img = cv2.imread("gamora_nebula.jpg")

img_in_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask
mask = maskGreen(img_in_hsv) + maskBlue(img_in_hsv)

# apply the mask
new_img = cv2.bitwise_and(img, img, mask=mask)

# convert to HSV
new_img_in_hsv = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)

# split the channels
new_h, new_s, new_v = cv2.split(new_img_in_hsv)

# change the h channel color
for i, row in enumerate(new_h):
  for j, pixel in enumerate(row):
    if isGreenInHSV(pixel):
      new_h.itemset(i, j, 120)
    elif isBlueHsv(pixel):
      new_h.itemset(i, j, 50)

# merge the channels
new_img = cv2.merge([new_h, new_s, new_v])

# convert to BGR
new_img = cv2.cvtColor(new_img, cv2.COLOR_HSV2BGR)

# show the image
cv2.imshow(title_window, new_img)

cv2.waitKey(0)

cv2.destroyAllWindows()










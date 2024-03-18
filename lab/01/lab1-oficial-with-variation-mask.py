import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

title_window = "Slider"
field_name_hue_low = "Hue_low"
field_name_hue_high = "Hue_high"

min_hue = 0
max_hue = 180


def get_value_cb():
  pass

# create slider here
cv2.namedWindow(title_window)
cv2.resizeWindow(title_window, 640, 480)
cv2.createTrackbar(field_name_hue_low, title_window, min_hue, max_hue, get_value_cb)
cv2.createTrackbar(field_name_hue_high, title_window, min_hue, max_hue, get_value_cb)

img = cv2.imread("gamora_nebula.jpg")

img_in_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
  # get the values from the trackbar
  hue_min = cv2.getTrackbarPos(field_name_hue_low, title_window)
  hue_max = cv2.getTrackbarPos(field_name_hue_high, title_window)

  # [H_min, S, V]
  lower_bound = np.array([hue_min, 0, 0])
  
  # [H_max, S, V]
  upper_bound = np.array([hue_max, 255, 255])

  # Detect an object based on the range of pixel values in the HSV color space
  # [hue_min, 0, 0] <= [H, S, V] <= [hue_max, 255, 255]
  mask = cv2.inRange(img_in_hsv, lower_bound, upper_bound)
  
  # apply the mask
  new_img = cv2.bitwise_and(img, img, mask=mask)

  # show the image
  cv2.imshow(title_window, new_img)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cv2.destroyAllWindows()










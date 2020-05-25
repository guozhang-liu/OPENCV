"""
Soble、Scharr算子，提取轮廓
"""

import cv2

img = cv2.imread("./pics/2.jpg")
img_soble = cv2.Scharr(img, ddepth=-1, dx=0, dy=1)   # y轴方向提亮轮廓
# img_soble = cv2.Sobel(img, ddepth=-1, dx=1, dy=0)  # x轴方向提亮轮廓

cv2.imshow("soble", img_soble)
cv2.waitKey(0)


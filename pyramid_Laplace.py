"""
Laplace金字塔
"""

import cv2

img = cv2.imread("./pics/1.jpg")
img_down = cv2.pyrDown(img)
img_up = cv2.pyrUp(img_down)
img_laplace = cv2.subtract(img, img_up)
img_laplace = cv2.convertScaleAbs(img_laplace, alpha=5, beta=1)  # 增加对比度

cv2.imshow("img_laplace", img_laplace)
cv2.waitKey(0)


"""
将两张图片像素按照权重相加
"""

import cv2

img1 = cv2.imread("./pics/1.jpg")
img2 = cv2.imread("./pics/6.jpg")

img = cv2.addWeighted(src1=img1, alpha=0.7, src2=img2, beta=0.7, gamma=0)
cv2.imshow("img", img)
cv2.waitKey(0)


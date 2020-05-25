"""
更改尺寸、旋转、镜像
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./pics/1.jpg")
# img = cv2.resize(img, dsize=(400, 400))
# img = cv2.transpose(img)
img = cv2.flip(img, -1)

cv2.imshow("pic", img)
cv2.waitKey(0)
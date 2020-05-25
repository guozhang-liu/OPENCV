"""
读图像
"""

import cv2

img = cv2.imread(r"./pics/1.jpg", flags=1)  # flags=0为灰度图，！=0则为彩图
cv2.imshow("1.jpg", img)
cv2.waitKey(0)

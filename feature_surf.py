"""
SURF特征提取算法（专利限制）
"""

import cv2

img = cv2.imread('./pics/32.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SURF_create()
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(img, kp, None, color=(0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey(0)
"""
HSV颜色mask
"""

import cv2
import numpy as np

# 打开图片
img = cv2.imread("./pics/1.jpg")

# 将BGR转为HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 提高对比度
img_contrast = cv2.convertScaleAbs(img, alpha=1.3, beta=1)

# 制作mask
lower_bar = np.array([100, 200, 100])
upper_bar = np.array([200, 255, 200])
mask = cv2.inRange(hsv, lower_bar, upper_bar)

# 过滤后图片
img_processed = cv2.bitwise_and(img, img,  mask=mask)

cv2.imshow("img", img)
cv2.imshow("img_contrast", img_contrast)
cv2.waitKey(0)

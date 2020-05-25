"""
unsharp mask 锐化处理
"""

import cv2

img = cv2.imread("./pics/1.jpg")

# 高斯模糊
img_blur = cv2.GaussianBlur(img, (3, 3), 0)
# 权重相加
img_usm = cv2.addWeighted(img, 2, img_blur, -1, 0)

cv2.imshow("original", img)
cv2.imshow("usm", img_usm)
cv2.waitKey(0)


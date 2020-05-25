"""
通过增加对比度更好的提取轮廓
"""

import cv2

img = cv2.imread("./pics/25.jpg")
img_abs = cv2.convertScaleAbs(img, alpha=6, beta=0)  # 提升对比度
img_GaussianBlur = cv2.GaussianBlur(img_abs, (5, 5), 0)  # 高斯模糊
img_canny = cv2.Canny(img_GaussianBlur, 50, 150)

cv2.imshow("img", img)
cv2.imshow("img_abs", img_abs)
cv2.imshow("img_canny", img_canny)
cv2.waitKey(0)


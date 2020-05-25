"""
边缘提取法---canny算法
"""

import cv2

img = cv2.imread("./pics/1.jpg")
img_GuassianBlur = cv2.GaussianBlur(img, (3, 3), 0)
img_canny = cv2.Canny(img_GuassianBlur, 100, 150)

cv2.imshow("canny", img_canny)
cv2.waitKey(0)



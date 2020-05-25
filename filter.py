"""
滤波器
"""

import cv2

img = cv2.imread("./pics/1.jpg")

i = 5
"""
低通滤波
"""
# dst = cv2.blur(img, ksize=(i, i))  # 均值模糊
# dst = cv2.GaussianBlur(img, ksize=(i, i), sigmaX=0)  # 高斯模糊
# dst = cv2.medianBlur(img, ksize=i)  # 中值滤波---椒盐噪声
# dst = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)  # 双边滤波

"""
高通滤波
"""
dst = cv2.Laplacian(img, ddepth=-1, ksize=1)


cv2.imshow("original", img)
cv2.imshow("blur", dst)
cv2.waitKey(0)


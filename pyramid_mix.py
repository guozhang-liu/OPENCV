"""
利用Gaussian和Laplace金字塔进行图片融合
"""

import cv2
import numpy as np

imgA = cv2.imread("./pics/21.jpg")
imgB = cv2.imread("./pics/22.jpg")

# 对imgA生成Gaussian金字塔
Gauss_A = [imgA]
for i in range(6):
    img = cv2.pyrDown(Gauss_A[i])
    Gauss_A.append(img)

# 对imgB生成Gaussian金字塔
Gauss_B = [imgB]
for i in range(6):
    img = cv2.pyrDown(Gauss_B[i])
    Gauss_B.append(img)

# 对imgA生成Laplace金字塔
Laplace_A = [Gauss_A[6]]
for i in range(6, 0, -1):
    up_sample = cv2.pyrUp(Gauss_A[i])
    laplace = cv2.subtract(Gauss_A[i-1], up_sample)
    Laplace_A.append(laplace)

# 对imgB生成Laplace金字塔
Laplace_B = [Gauss_B[6]]
for i in range(6, 0, -1):
    up_sample = cv2.pyrUp(Gauss_B[i])
    laplace = cv2.subtract(Gauss_B[i-1], up_sample)
    Laplace_B.append(laplace)

# 对imgA和imgB的Laplace金字塔进行切割拼接
Laplace_mix = []
for i, (lapA, lapB) in enumerate(zip(Laplace_A, Laplace_B)):
    rows, cols, channels = lapA.shape
    lap_a = lapA[:, :cols//2]
    lap_b = lapB[:, cols//2:]
    lap_mix = np.hstack((lap_a, lap_b))
    Laplace_mix.append(lap_mix)

# 重构图像
ls = Laplace_mix[0]
for i in range(1, 7):
    ls = cv2.pyrUp(ls)
    ls = cv2.add(ls, Laplace_mix[i])

# 直接拼接
rows, cols, channels, = imgA.shape
real = np.hstack((imgA[:, :cols // 2], imgB[:, cols // 2:]))

cv2.imshow("Laplace", ls)
cv2.imshow("Real", real)
cv2.waitKey(0)


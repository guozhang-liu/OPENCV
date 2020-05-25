"""
仿射变换
"""

import cv2
import numpy as np

src = cv2.imread("./pics/1.jpg")
H, W, C = src.shape
"""
自定义仿射矩阵
"""
# 分别向x轴y轴分别平移50
M = np.float32([[1, 0, 50], [0, 1, 50]])
# x轴y轴分别缩小为原来0.5倍
N = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
# x轴缩小0.5倍且沿y轴翻转再沿x轴正方向移动W//2的距离，y轴缩小0.5倍
P = np.float32([[-0.5, 0, W//2], [0, 0.5, 0]])
# 沿x轴变形0.5倍
Q = np.float32([[1, 0.5, 0], [0, 1, 0]])

"""
利用opencv生成仿射矩阵
"""
# 以H//2，W//2为中心，旋转45°， 缩放0.7倍
K = cv2.getRotationMatrix2D(center=(H//2, W//2), angle=0, scale=0.5)

# 完成仿射变换
dst = cv2.warpAffine(src, K, dsize=(W, H))

cv2.imshow("original", src)
cv2.imshow("transformed", dst)
cv2.waitKey(0)

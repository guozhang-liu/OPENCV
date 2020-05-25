"""
写图像
"""

import cv2
import numpy as np

matrix = np.empty((200, 200, 3))
matrix[..., 0] = 255
# matrix[..., 1] = 0
# matrix[..., 2] = 0
matrix = matrix[..., ::-1]   # 通道倒序

img = cv2.imwrite("img_write.png", matrix)   # 图片一定要加后缀“.jpg”....

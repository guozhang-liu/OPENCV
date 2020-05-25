"""
opencv中的加减运算
"""

import cv2
import numpy as np

a = np.uint8([10, 11, 12])  # uint8范围为0~255
b = np.uint8([1, 20, 3])

print(cv2.add(a, b))
print(cv2.subtract(a, b))



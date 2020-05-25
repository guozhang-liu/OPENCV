"""
OTSU：大津算法。自动阀值，二值化
"""

import cv2

img = cv2.imread("./pics/1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)  # 先转为灰度图
# ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  #  超过阈值部分取maxval（最大值），否则取0
# ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  #  THRESH_BINARY的反转
# ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)  # 大于阈值部分设为阈值，否则不变
# ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_TOZERO | cv2.THRESH_OTSU)  # 大于阈值部分不改变，否则设为0
ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_TOZERO_INV | cv2.THRESH_OTSU)  # THRESH_TOZERO的反转

cv2.imshow("Gray", img_gray)
cv2.imshow("Binary", img_binary)
cv2.waitKey(0)

"""
计算图形轮廓内面积、重心、周长
"""

import cv2

img = cv2.imread("./pics/26.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contour, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 重心
M = cv2.moments(contour[0])  # 矩
x, y = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
print("重心：", x, y)

# 面积
area = cv2.contourArea(contour[0])
print("面积：", area)

# 周长
perimeter = cv2.arcLength(contour[0], True)
print("周长：", perimeter)


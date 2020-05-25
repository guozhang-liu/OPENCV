"""
绘制不规则图形的边界矩形、最小矩形、最小外接圆
"""


import numpy as np
import cv2
img = cv2.imread("./pics/16.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contour, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制边界矩形
x, y, w, h = cv2.boundingRect(contour[0])
img_contour = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# 绘制最小矩形
rect = cv2.minAreaRect(contour[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
img_contour = cv2.drawContours(img, [box], -1, (255, 0, 0), 2)

# 绘制外界圆
(x, y), radius = cv2.minEnclosingCircle(contour[0])
center = (int(x), int(y))
radius = int(radius)
img_contour = cv2.circle(img, center, radius, (0, 255, 0), 2)

cv2.imshow("contours", img_contour)
cv2.waitKey(0)

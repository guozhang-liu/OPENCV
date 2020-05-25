"""
判断图形是否为凸，画出图形凸包曲线
"""

import cv2

img = cv2.imread("./pics/26.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

contour, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contour[0])
img_contour = cv2.drawContours(img, [hull], -1, (0, 0, 255), 2)

print(cv2.isContourConvex(contour[0]), cv2.isContourConvex(hull))  # 判断图形及凸包曲线是否为凸
cv2.imshow("img_contour", img_contour)
cv2.waitKey(0)


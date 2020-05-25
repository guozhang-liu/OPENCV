"""
对于不规则图形，绘制其大致轮廓
"""

import cv2

img = cv2.imread("./pics/26.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contour, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 40  # 精度
approx = cv2.approxPolyDP(contour[0], epsilon, True)

img_contour = cv2.drawContours(img, [approx], -1, (255, 0, 0), 2)
cv2.imshow("contour", img_contour)
cv2.waitKey(0)



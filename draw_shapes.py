"""
图像上画型状
"""

import cv2
import numpy as np

img = cv2.imread("./pics/1.jpg")

# 画直线
cv2.line(img, (10, 10), (50, 50), color=(255, 0, 0), thickness=3,)
# 画矩形
cv2.rectangle(img, (25, 34), (56, 78), color=(0, 123, 234), thickness=3)
# 画圆圈
cv2.circle(img, (160, 190), 100, color=(23, 45, 190), thickness=2)
# 画椭圆
cv2.ellipse(img, (100, 100), (100, 50), 0, 0, 360, color=(0, 0, 255), thickness=2)
# 写字
cv2.putText(img, "beautiful_girl", (10, 30), cv2.FONT_HERSHEY_PLAIN, fontScale=4, color=(11, 34, 56),  lineType=cv2.LINE_AA)
# 画多边形
points = np.array([[2, 3], [34, 44], [56, 90], [90, 180]])
cv2.polylines(img, [points], True, color=(255, 199, 0), thickness=2)


cv2.imshow("1", img)
cv2.waitKey(0)

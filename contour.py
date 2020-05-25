"""
查找，绘制图像轮廓
"""

import cv2

img = cv2.imread("./pics/14.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 自适应二值化

contour, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 简化轮廓
# contour, hierarchy = cv2.findContours(the, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 非简化
print(contour)
img_contour = cv2.drawContours(img, contour, -1, (0, 255, 0), 2)  # 绘制轮廓
print(len(contour[0]))

cv2.imshow("..", img_contour)
cv2.waitKey(0)


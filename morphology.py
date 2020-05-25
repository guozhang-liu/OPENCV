"""
形态变换
"""

import cv2

img = cv2.imread("./pics/4.jpg")
# 核
i = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (i, i))

# dst = cv2.erode(img, kernel)  # 腐蚀
# dst = cv2.dilate(img, kernel)  # 膨胀
# dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # 开操作（先腐蚀后膨胀）---去噪
# dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 闭操作（先膨胀后腐蚀）---补洞
# dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # 梯度操作---提取轮廓
# dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)  # 顶帽操作---提取噪点
dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel=(3, 3))  # 黑帽操作---提取漏洞

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)

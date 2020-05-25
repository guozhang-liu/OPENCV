import cv2

img1 = cv2.imread("./pics/1.jpg")
img2 = cv2.imread("./pics/6.jpg")

H, W, C = img2.shape
img1 = img1[:H, :W, :]

""" 
制作掩膜
"""
# 转灰度图
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# 二值化
ret, mask = cv2.threshold(img2_gray, 10, 255, cv2.THRESH_BINARY)
# 用位运算将白字转为黑字
mask_inv = cv2.bitwise_not(mask)
# 用位运算-与将掩膜与图片合并
img_combine = cv2.bitwise_and(img1, img1, mask=mask_inv)

cv2.imshow("img_combine", img_combine)
cv2.imshow("img1", img1)
cv2.waitKey(0)


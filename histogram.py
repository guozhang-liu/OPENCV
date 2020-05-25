"""
绘制图片颜色直方图
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./pics/1.jpg')
# img[...,0]=0  # 屏蔽通道B
# img[...,1]=0  # 屏蔽通道G
cv2.imshow("...", img)

img_B = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(img_B, label='B', color='b')

img_G = cv2.calcHist([img], [1], None, [256], [0, 256])
plt.plot(img_G, label='G', color='g')
#
img_R = cv2.calcHist([img], [2], None, [256], [0, 256])
plt.plot(img_R, label='R', color='r')

plt.show()

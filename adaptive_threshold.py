"""
自适应阀值
"""

import cv2
import matplotlib.pyplot as plt


th1 = cv2.imread("./pics/2.jpg", 0)
th1 = cv2.GaussianBlur(th1, ksize=(5, 5), sigmaX=0)  # 高斯模糊
ret, th2 = cv2.threshold(th1, thresh=127, maxval=255, type=cv2.THRESH_BINARY)  # 阀值127
th3 = cv2.adaptiveThreshold(th1, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,  # 平均阀值
                            thresholdType=cv2.THRESH_BINARY, C=7, blockSize=11)
th4 = cv2.adaptiveThreshold(th1, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # 高斯阀值
                            thresholdType=cv2.THRESH_BINARY, C=7, blockSize=11)


text = ["Original", "Threshold", "Adaptive_Mean", "Adaptive_Gaussian"]
img = [th1, th2, th3, th4]


for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(img[i], "gray")
    plt.title(text[i])
    plt.axis("off")
plt.show()

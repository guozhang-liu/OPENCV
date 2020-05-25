"""
傅里叶变换opencv实现：时域转频域——过滤高频信号——转变回时域
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pics/9.jpg", 0)  # 第一步：读取图片（以灰度图的形式）
img_float = np.float32(img)  # 第二步：将图片像素值转换为浮点型
img_dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)  # 第三步：进行傅里叶变换flags为具体傅里叶变换方法
dft_center = np.fft.fftshift(img_dft)  # 第四步：将低频信号移到图像正中央（频域图）

# 使用cv2.magnitude将实部和虚部转换为实部，乘以20是为了使得结果更大
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_center[:, :, 0], dft_center[:, :, 1]))
# 画出原图的灰度图、频域图
plt.figure(figsize=(10, 10))
plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

row, col = img.shape  # 第五步：声明频域图中心点
crow, ccol = row//2, col//2

mask = np.zeros((row, col, 2), np.uint8)  # 第六步：制作掩膜。因为傅里叶变换后生成img_dft分为实部、虚部，此处形状为(row, col, 2)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1  # 将零矩阵中间60×60的区域变为1

img_masked = dft_center*mask  # 第七步：保留原图中间的低频部分，过滤掉周围的高频部分
img_idf = np.fft.ifftshift(img_masked)  # 第八步：将低频还原至原来位置
img_idf = cv2.idft(img_idf)  # 第九步：进行傅里叶变换逆变换
img_back = cv2.magnitude(img_idf[:, :, 0], img_idf[:, :, 1])  # 第十步：将频域图转换为时域图

# 画出频率过滤掉高频信号后转为时域的原图及其灰度图
plt.subplot(223), plt.imshow(img_back, cmap='gray')
plt.title('Output GaryImage'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_back)
plt.title('Output Image'), plt.xticks([]), plt.yticks([])

plt.show()

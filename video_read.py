"""
读视频
"""

import cv2

video = cv2.VideoCapture(0)
while True:
    """
    逐帧捕获
    """
    ret, frame = video.read()  # 返回值ret为布尔型，视频是否可用
    cv2.imshow("frame", frame)
    if cv2.waitKey(30) & 0xFF == ord("a"):
        break
video.release()
cv2.destroyAllWindows()

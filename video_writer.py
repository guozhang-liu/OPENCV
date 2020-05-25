"""
写视频
"""

import cv2

video = cv2.VideoCapture(0)  # read the camera
size = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # opencv-N,W,H,C
save_path = "./Output/camera_detection.avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # 编码格式
fps = 12  # 帧率
out = cv2.VideoWriter(save_path, fourcc, fps, size)

while True:
    """
    逐帧捕获
    """
    ret, frame = video.read()  # 返回值ret为布尔型，视频是否可用
    out.write(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(30) & 0xFF == ord("a"):
        break
video.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

# 帧率
pTime = 0
cTime = 0
# 开启摄像头，如果有两个摄像头，则参数为1
cap = cv2.VideoCapture(0)
# 调用手势识别模块
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

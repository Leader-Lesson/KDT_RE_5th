import cv2

capture = cv2.VideoCapture(0) 

# 1. 캠 화면 크기 조절 (숫자 조절)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 

# 2. 캠 화면 프레임 조절 (waitKey의 숫자로 조절) 
while cv2.waitKey(10) < 0: 
    ret, frame = capture.read()
    if not ret: break
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
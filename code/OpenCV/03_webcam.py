import cv2
import os

# 장치의 0번째 카메라를 불러옴
cap = cv2.VideoCapture(0)

if not cap.isOpened():  # 카메라가 정상적으로 열리지 않았을 경우
    print("카메라가 없어요")
    exit()

# 카메라 사진 찍기
while cap.isOpened():
    ret, img = cap.read()

    if ret:
        cv2.imshow('camera', img)

        # 10ms 동안 키 입력을 대기
        # 키가 입력되면 (-1이 아니면) 사진을 저장하고 종료
        if cv2.waitKey(10) != -1:
            cv2.imwrite(f'{os.path.dirname(__file__)}/output/capture.jpg', img)
            break

cap.release()
cv2.destroyAllWindows()

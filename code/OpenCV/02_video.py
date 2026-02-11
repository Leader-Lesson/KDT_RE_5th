import cv2
import os

# 비디오 파일 또는 웹캠 연결
path = os.path.join(os.path.dirname(__file__), "images", "video.mp4")
cap = cv2.VideoCapture(path)  # 웹캠은 0 입력

# while cap.isOpened():  # 영상이 정상적으로 열려있는 동안 반복
#     ret, frame = cap.read()  # 프레임 읽기

#     if not ret:  # 더 이상 프레임이 없으면 종료
#         break

#     cv2.imshow("Video Player", frame)

#     # 'q' 키를 누르면 종료 (33ms 대기로 약 30fps 유지)
#     if cv2.waitKey(33) == ord('q'):
#         break

# cap.release()  # 자원 해제
# cv2.destroyAllWindows()


# 실습 2 - 속도 조절

# 영상의 FPS (초당 프레임 수) 정보 얻기
fps = cap.get(cv2.CAP_PROP_FPS)
total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# 재생 속도 성정을 위한 변수 (기본값)
# 1000 // fps 기본
delay = int(1000 // fps)

while True:
    # 루프 재생
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == total_frame - 1:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("VideoFrame", frame)
    # 1. 일반 속도: cv2.waitKey(delay)
    # 2. 2배 빠른 속도: cv2.waitKey(delay // 2)
    # 3. 2배 느린 속도: cv2.waitKey(delay * 2)
    if cv2.waitKey(delay // 2) >= 0:
        break

cap.release()
cv2.destroyAllWindows()

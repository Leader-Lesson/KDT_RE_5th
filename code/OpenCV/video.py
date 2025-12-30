import cv2

# # 비디오 파일 또는 웹캠(0) 연결
# cap = cv2.VideoCapture("images/video.mp4") # 웹캠은 0 입력

# while cap.isOpened(): # 영상이 정상적으로 열려있는 동안 반복
#     ret, frame = cap.read() # 프레임 읽기
    
#     if not ret: # 더 이상 프레임이 없으면 종료 
#         break
        
#     cv2.imshow("Video Player", frame)
    
#     # 'q' 키를 누르면 종료 (33ms 대기로 약 30fps 유지)
#     if cv2.waitKey(33) == ord('q'):
#         break

# cap.release() # 자원 해제
# cv2.destroyAllWindows()



# 실습 2
# 영상 파일 읽기
capture = cv2.VideoCapture('images/video.mp4') 

# 영상의 FPS(초당 프레임 수) 정보 얻기
fps = capture.get(cv2.CAP_PROP_FPS) 
total_frame = capture.get(cv2.CAP_PROP_FRAME_COUNT) 

# 재생 속도 설정을 위한 변수 (기본값)
# 1000 // fps 보다 작으면 빠름, 크면 느림
delay = int(1000 // fps) 

while True:
  # 루프 재생 설정: 마지막 프레임이면 처음으로 되돌림
  if capture.get(cv2.CAP_PROP_POS_FRAMES) == total_frame - 1: 
    capture.set(cv2.CAP_PROP_POS_FRAMES, 0) 

  ret, frame = capture.read()
  if not ret: 
    break

  cv2.imshow("VideoFrame", frame) 

  # --- 프레임 조절 핵심 부분 ---
  # 1. 일반 속도: cv2.waitKey(delay)
  # 2. 2배 빠른 속도: cv2.waitKey(delay // 2)
  # 3. 2배 느린 속도: cv2.waitKey(delay * 2)
  
  if cv2.waitKey(delay) >= 0: # 아무 키나 누르면 종료
    break

capture.release() 
cv2.destroyAllWindows()
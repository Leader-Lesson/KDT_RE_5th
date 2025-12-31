import cv2

# 원본 영상 불러오기
cap = cv2.VideoCapture("images/video.mp4")

# 1. VideoWriter 설정을 위한 정보 획득 
fourcc = cv2.VideoWriter_fourcc(*"H264") # 코덱 설정
fps = cap.get(cv2.CAP_PROP_FPS) # 원본 FPS 가져오기
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 가로 크기
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 세로 크기

# 2. VideoWriter 객체 생성 
# 주의: "output" 폴더가 미리 생성되어 있어야 합니다.
out = cv2.VideoWriter("output/video.mp4", fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 3. 프레임 저장 
    # 주의: 이 방식은 소리는 저장되지 않습니다.
    out.write(frame) 
    
    cv2.imshow("Video", frame)
    
    # 'q' 키를 누르면 종료 
    # 대기 시간 계산: $1000 / fps$ ms
    if cv2.waitKey(int(1000/fps)) == ord("q"):
        cv2.imwrite("output/capture_video.jpg", frame)
        break

# 4. 자원 해제 (반드시 out도 release 해야 파일이 정상 저장됨) 
out.release() 
cap.release()
cv2.destroyAllWindows()

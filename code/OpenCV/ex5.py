import cv2

cap = cv2.VideoCapture('images/video.mp4')

while cap.isOpened():   
    ret, frame = cap.read() 
    if not ret:
        break
    
    # 영상 프레임을 1.5배로 리사이즈    
    # 보간법으로 INTER_CUBIC 사용 (확대 시 추천) 
    resized_frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow("Resized Video", resized_frame)  
    
    if cv2.waitKey(33) == ord('q'):
        break

cap.release()   
cv2.destroyAllWindows() 
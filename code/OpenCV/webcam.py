import cv2

# 장치의 0번째 카메라를 불러옴 
cap = cv2.VideoCapture(0)

if not cap.isOpened(): # 카메라가 정상적으로 열리지 않았을 경우
  print("카메라가 없어요")
  exit()

# while True: # 무한 반복
#   ret, frame = cap.read() # 카메라로부터 프레임 읽기 

#   if not ret:
#     print("불러올 이미지가 없어요")
#     break

#   cv2.imshow("My Camera", frame)

#   # 'q' 키를 누르면 종료 (1ms 대기)
#   if cv2.waitKey(1) == ord("q"):
#     print("사용자 입력에 의해 종료되었어요.")
#     break
  
  
# 카메라 사진 찍기
while cap.isOpened():
  ret, img = cap.read()
  
  if ret:
    cv2.imshow('camera', img)
    
    # 10ms 동안 키 입력을 대기
    # 키가 입력되면 (-1이 아니면) 사진을 저장하고 종료
    if cv2.waitKey(10) != -1:
      cv2.imwrite('output/capture.jpg', img) # 사진 저장 폴더 미리 생성 필요
      break

cap.release()
cv2.destroyAllWindows()
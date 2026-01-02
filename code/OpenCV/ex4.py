import cv2

# 1. 이미지 읽기 (흑백으로 로드) 
image = cv2.imread('images/dog.jpg', cv2.IMREAD_GRAYSCALE)

# 2. 흑백 반전 (각 픽셀 값을 255에서 뺌) 
# 픽셀 데이터 타입인 uint8(0~255)을 기반으로 계산됩니다.
inverted_image = 255 - image

# 3. 결과 출력 
cv2.imshow("Original Image", image)
cv2.imshow("Inverted Image", inverted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
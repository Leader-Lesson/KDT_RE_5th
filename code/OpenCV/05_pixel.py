import cv2
import numpy as np

# 가로 640, 세로 460 크기의 검은색 빈 화면 생성
img = np.zeros((460, 640, 3), dtype=np.uint8)

# 일부 영역 (세로 100~200, 가로 200~300)을 흰색으로 색칠
# BGR 순서이므로
img[100:200, 200:300] = (255, 255, 255)

cv2.imshow("Drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 채널 분리와 병합
image = cv2.imread("OpenCV/images/rgb.png")

# 채널 분리 (B,G,R 순서)
b, g, r = cv2.split(image)

# 개별 채널 출력
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 색상 공간 변환 (BGR -> Gray)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Drawing2", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 분리된 채널을 리스트로 묶어 병합
merged_image = cv2.merge([b, g, r])

# 결과 출력
cv2.imshow("Merged Image", merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

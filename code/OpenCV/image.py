import cv2

# 이미지 읽기
# img = cv2.imread("images/dog.jpg")
# # 이미지 창에 표시
# cv2.imshow("Image Window", img)
# # 키보드 입력 대기 (0은 무한 대기)
# key = cv2.waitKey(0)
# print("Pressed key code:", key)
# # 모든 창 닫기
# cv2.destroyAllWindows()

# # 채널 3 (R, G, B)
img_default = cv2.imread("images/dog.jpg", cv2.IMREAD_COLOR)
# 채널 없음 (그레이스케일)
img_grayscale = cv2.imread("images/dog.jpg", cv2.IMREAD_GRAYSCALE)
# 채널 4 (Alpha 값 포함)
img_unchanged = cv2.imread("images/dog.jpg", cv2.IMREAD_UNCHANGED)

# cv2.imshow("Default Image", img_default)
# cv2.imshow("Grayscale Image", img_grayscale)
# cv2.imshow("Unchanged Image", img_unchanged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

logo_defualt = cv2.imread("images/logo.png", cv2.IMREAD_COLOR)
logo_unchanged = cv2.imread("images/logo.png", cv2.IMREAD_UNCHANGED)

cv2.imshow("Logo Default", logo_defualt)
cv2.imshow("Logo Unchanged", logo_unchanged)
print("Logo Shape (Unchanged):", logo_unchanged.shape) 
cv2.waitKey(0)
cv2.destroyAllWindows()


# /////////////
# 이미지 Shape
img = cv2.imread("images/dog.jpg")
print("Image Shape:", img.shape)  # (높이, 너비, 채널 수)
height, width, channels = img.shape
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

print("IMREAD_COLOR:", img_default.shape)
print("IMREAD_GRAYSCALE:", img_grayscale.shape)
print("IMREAD_UNCHANGED:", img_unchanged.shape)
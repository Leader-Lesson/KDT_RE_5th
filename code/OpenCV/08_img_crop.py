import cv2

image = cv2.imread('OpenCV/images/dog.jpg')

# 이미지 자르기
img_crop = image[100:200, 100:400]


cv2.imshow('Origin', image)
cv2.imshow('Crop', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

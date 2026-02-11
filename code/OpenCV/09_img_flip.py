import cv2

image = cv2.imread('OpenCV/images/dog.jpg')

# 좌우 반전
img_flip = cv2.flip(image, 1)  # > 0 : y축 반전

cv2.imshow('Flip', img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

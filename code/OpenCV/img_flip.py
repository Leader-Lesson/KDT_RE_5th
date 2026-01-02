import cv2

img = cv2.imread('images/dog.jpg')
# 좌우 반전 예시
img_flip = cv2.flip(img, 1) 

cv2.imshow('Flip', img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
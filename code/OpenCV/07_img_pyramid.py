import cv2

image = cv2.imread('OpenCV/images/dog.jpg')

# 2배 확대
img_up = cv2.pyrUp(image)
# 2배 축소
img_down = cv2.pyrDown(image)

cv2.imshow('Up', img_up)
cv2.imshow('Down', img_down)
cv2.waitKey(0)
cv2.destroyAllWindows()

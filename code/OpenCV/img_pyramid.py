import cv2

img = cv2.imread('images/dog.jpg')

# 2배 확대
img_up = cv2.pyrUp(img)
# 2배 축소
img_down = cv2.pyrDown(img)

cv2.imshow('Up', img_up)
cv2.imshow('Down', img_down)
cv2.waitKey(0)
cv2.destroyAllWindows()
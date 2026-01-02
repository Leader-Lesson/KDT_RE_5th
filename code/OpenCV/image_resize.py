import cv2

img = cv2.imread('images/dog.jpg') 

# 1. 고정 크기로 조정 (가로 320, 세로 240) 
dst_fixed = cv2.resize(img, (320, 240)) 

# 2. 비율로 조정 (가로 0.5배, 세로 0.5배)
dst_ratio = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Fixed Resize", dst_fixed)   
cv2.imshow("Ratio Resize", dst_ratio)
cv2.waitKey(0)
cv2.destroyAllWindows()
